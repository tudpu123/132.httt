#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
客服后端API服务器
为深夜密友交友平台提供客服系统后端支持
"""

import json
import os
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 数据文件路径
DATA_FILE = 'customer_service_data.json'

# 初始化数据文件
def init_data_file():
    if not os.path.exists(DATA_FILE):
        initial_data = {
            "conversations": [],
            "customers": [],
            "agents": [
                {
                    "id": 1,
                    "name": "客服小助手",
                    "status": "online",
                    "last_active": datetime.now().isoformat()
                }
            ],
            "settings": {
                "auto_reply_enabled": True,
                "auto_reply_messages": [
                    "您好，很高兴为您服务！",
                    "我理解您的问题，让我为您解答。",
                    "感谢您的咨询，我们会尽快处理。",
                    "这个问题需要进一步了解，请稍等。",
                    "我们已经收到您的反馈，会尽快回复。",
                    "建议您查看常见问题解答，可能对您有帮助。",
                    "感谢您的耐心等待，正在为您查询。",
                    "这个问题比较常见，让我为您详细说明。"
                ],
                "qq_contact": "1158980053"
            }
        }
        save_data(initial_data)

# 保存数据到文件
def save_data(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存数据失败: {e}")
        return False

# 从文件加载数据
def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载数据失败: {e}")
        return None

# 生成唯一ID
def generate_id():
    return int(time.time() * 1000)

# API路由

@app.route('/')
def index():
    """客服API首页"""
    return jsonify({
        "service": "深夜密友客服系统API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "客服对话": "/api/conversations",
            "发送消息": "/api/send_message",
            "获取对话": "/api/conversation/<conversation_id>",
            "客服状态": "/api/agent_status"
        }
    })

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    """获取所有对话列表"""
    data = load_data()
    if not data:
        return jsonify({"error": "数据加载失败"}), 500
    
    # 只返回基本信息，不包含详细消息
    conversations = []
    for conv in data.get("conversations", []):
        conversations.append({
            "id": conv["id"],
            "customer_name": conv["customer_name"],
            "status": conv["status"],
            "last_message": conv["messages"][-1]["content"] if conv["messages"] else "",
            "last_active": conv["last_active"],
            "message_count": len(conv["messages"])
        })
    
    return jsonify({"conversations": conversations})

@app.route('/api/conversation/<int:conversation_id>', methods=['GET'])
def get_conversation(conversation_id):
    """获取特定对话的详细信息"""
    data = load_data()
    if not data:
        return jsonify({"error": "数据加载失败"}), 500
    
    for conv in data.get("conversations", []):
        if conv["id"] == conversation_id:
            return jsonify({"conversation": conv})
    
    return jsonify({"error": "对话不存在"}), 404

@app.route('/api/send_message', methods=['POST'])
def send_message():
    """发送消息"""
    try:
        message_data = request.get_json()
        
        # 验证必需字段
        required_fields = ['content', 'sender_type']
        for field in required_fields:
            if field not in message_data:
                return jsonify({"error": f"缺少必需字段: {field}"}), 400
        
        data = load_data()
        if not data:
            return jsonify({"error": "数据加载失败"}), 500
        
        conversation_id = message_data.get('conversation_id')
        customer_name = message_data.get('customer_name', '匿名用户')
        
        # 查找或创建对话
        conversation = None
        if conversation_id:
            for conv in data["conversations"]:
                if conv["id"] == conversation_id:
                    conversation = conv
                    break
        
        if not conversation:
            # 创建新对话
            conversation_id = generate_id()
            conversation = {
                "id": conversation_id,
                "customer_name": customer_name,
                "status": "active",
                "created_at": datetime.now().isoformat(),
                "last_active": datetime.now().isoformat(),
                "messages": []
            }
            data["conversations"].append(conversation)
        
        # 添加消息
        message = {
            "id": generate_id(),
            "content": message_data['content'],
            "sender_type": message_data['sender_type'],  # 'customer' 或 'agent'
            "timestamp": datetime.now().isoformat(),
            "read": False
        }
        conversation["messages"].append(message)
        conversation["last_active"] = datetime.now().isoformat()
        
        # 如果是客户消息，自动回复
        if message_data['sender_type'] == 'customer':
            # 模拟客服回复
            auto_reply = {
                "id": generate_id(),
                "content": get_auto_reply_message(data),
                "sender_type": "agent",
                "timestamp": datetime.now().isoformat(),
                "read": False
            }
            conversation["messages"].append(auto_reply)
            
            # 偶尔添加QQ提示
            if len(conversation["messages"]) % 3 == 0:
                qq_message = {
                    "id": generate_id(),
                    "content": f"如果长时间没有恢复消息请添加客服QQ{data['settings']['qq_contact']}",
                    "sender_type": "agent",
                    "timestamp": datetime.now().isoformat(),
                    "read": False
                }
                conversation["messages"].append(qq_message)
        
        # 保存数据
        if save_data(data):
            return jsonify({
                "success": True,
                "conversation_id": conversation["id"],
                "message_id": message["id"]
            })
        else:
            return jsonify({"error": "消息发送失败"}), 500
            
    except Exception as e:
        return jsonify({"error": f"服务器错误: {str(e)}"}), 500

def get_auto_reply_message(data):
    """获取自动回复消息"""
    messages = data['settings']['auto_reply_messages']
    import random
    return random.choice(messages)

@app.route('/api/agent_status', methods=['GET'])
def get_agent_status():
    """获取客服状态"""
    data = load_data()
    if not data:
        return jsonify({"error": "数据加载失败"}), 500
    
    agents = data.get("agents", [])
    return jsonify({"agents": agents})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """获取客服系统统计信息"""
    data = load_data()
    if not data:
        return jsonify({"error": "数据加载失败"}), 500
    
    conversations = data.get("conversations", [])
    active_conversations = [c for c in conversations if c["status"] == "active"]
    total_messages = sum(len(c["messages"]) for c in conversations)
    
    stats = {
        "total_conversations": len(conversations),
        "active_conversations": len(active_conversations),
        "total_messages": total_messages,
        "online_agents": len([a for a in data.get("agents", []) if a["status"] == "online"])
    }
    
    return jsonify(stats)

@app.route('/admin')
def admin_dashboard():
    """客服管理后台"""
    html = '''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>客服管理后台 - 深夜密友</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: Arial, sans-serif; background: #f5f5f5; }
            .header { background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: white; padding: 20px; text-align: center; }
            .container { max-width: 1200px; margin: 20px auto; padding: 20px; }
            .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px; }
            .stat-card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; }
            .stat-number { font-size: 2em; font-weight: bold; color: #8b5cf6; }
            .conversation-list { background: white; border-radius: 10px; padding: 20px; }
            .conversation-item { border-bottom: 1px solid #eee; padding: 15px 0; }
            .conversation-item:last-child { border-bottom: none; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1><i class="fas fa-headset"></i> 客服管理后台</h1>
            <p>深夜密友交友平台 - 客服系统管理</p>
        </div>
        <div class="container">
            <div class="stats-grid" id="stats">
                <div class="stat-card">
                    <div class="stat-number" id="total-conversations">0</div>
                    <div>总对话数</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="active-conversations">0</div>
                    <div>活跃对话</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="total-messages">0</div>
                    <div>总消息数</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" id="online-agents">0</div>
                    <div>在线客服</div>
                </div>
            </div>
            
            <div class="conversation-list">
                <h2>最近对话</h2>
                <div id="conversations"></div>
            </div>
        </div>
        
        <script>
            async function loadStats() {
                try {
                    const response = await fetch('/api/stats');
                    const stats = await response.json();
                    
                    document.getElementById('total-conversations').textContent = stats.total_conversations;
                    document.getElementById('active-conversations').textContent = stats.active_conversations;
                    document.getElementById('total-messages').textContent = stats.total_messages;
                    document.getElementById('online-agents').textContent = stats.online_agents;
                } catch (error) {
                    console.error('加载统计信息失败:', error);
                }
            }
            
            async function loadConversations() {
                try {
                    const response = await fetch('/api/conversations');
                    const data = await response.json();
                    
                    const container = document.getElementById('conversations');
                    container.innerHTML = '';
                    
                    data.conversations.forEach(conv => {
                        const item = document.createElement('div');
                        item.className = 'conversation-item';
                        item.innerHTML = `
                            <strong>${conv.customer_name}</strong>
                            <span style="float: right; color: #666;">${new Date(conv.last_active).toLocaleString()}</span>
                            <br>
                            <small>${conv.last_message}</small>
                        `;
                        container.appendChild(item);
                    });
                } catch (error) {
                    console.error('加载对话列表失败:', error);
                }
            }
            
            // 页面加载时获取数据
            loadStats();
            loadConversations();
            
            // 每30秒刷新一次数据
            setInterval(() => {
                loadStats();
                loadConversations();
            }, 30000);
        </script>
    </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    # 初始化数据文件
    init_data_file()
    
    print("深夜密友客服系统API服务器启动中...")
    print("服务地址: http://localhost:5000")
    print("API文档: http://localhost:5000")
    print("管理后台: http://localhost:5000/admin")
    print("=" * 50)
    
    try:
        app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
    except Exception as e:
        print(f"服务器启动失败: {e}")
        print("尝试使用备用端口...")
        app.run(host='0.0.0.0', port=5001, debug=False, threaded=True)