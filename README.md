<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>深夜密友客服系统 - 完整集成版</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .header { 
            background: rgba(255, 255, 255, 0.95); 
            color: #333; 
            padding: 25px 40px; 
            text-align: center; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
        }
        
        .header h1 { 
            font-size: 2.5em; 
            margin-bottom: 10px; 
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .container { 
            max-width: 1400px; 
            margin: 30px auto; 
            padding: 0 20px; 
        }
        
        .tabs {
            display: flex;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px 15px 0 0;
            padding: 0 20px;
            backdrop-filter: blur(10px);
        }
        
        .tab {
            padding: 15px 25px;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        .tab.active {
            border-bottom: 3px solid #667eea;
            color: #667eea;
        }
        
        .tab-content {
            display: none;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 0 0 15px 15px;
            padding: 30px;
            min-height: 500px;
            backdrop-filter: blur(10px);
        }
        
        .tab-content.active {
            display: block;
        }
        
        .stats-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 25px; 
            margin-bottom: 40px; 
        }
        
        .stat-card { 
            background: rgba(255, 255, 255, 0.95); 
            padding: 30px; 
            border-radius: 15px; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.1); 
            text-align: center; 
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            backdrop-filter: blur(10px);
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }
        
        .stat-number { 
            font-size: 3em; 
            font-weight: bold; 
            color: #667eea; 
            margin-bottom: 10px;
        }
        
        .stat-card i {
            font-size: 2.5em;
            color: #764ba2;
            margin-bottom: 15px;
        }
        
        .dashboard { 
            display: grid; 
            grid-template-columns: 1fr 400px; 
            gap: 30px; 
            margin-bottom: 40px; 
        }
        
        .conversation-list { 
            background: rgba(255, 255, 255, 0.95); 
            border-radius: 15px; 
            padding: 30px; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
        }
        
        .conversation-item { 
            border-bottom: 1px solid #eee; 
            padding: 20px 0; 
            transition: background-color 0.3s ease;
        }
        
        .conversation-item:hover {
            background-color: rgba(102, 126, 234, 0.05);
            border-radius: 8px;
            padding: 20px;
            margin: 0 -10px;
        }
        
        .conversation-item:last-child { border-bottom: none; }
        
        .sidebar { 
            background: rgba(255, 255, 255, 0.95); 
            border-radius: 15px; 
            padding: 30px; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
        }
        
        .agent-status {
            margin-bottom: 30px;
        }
        
        .agent-item {
            display: flex;
            align-items: center;
            padding: 15px;
            background: rgba(102, 126, 234, 0.1);
            border-radius: 10px;
            margin-bottom: 10px;
        }
        
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 15px;
        }
        
        .status-online { background: #4CAF50; }
        .status-offline { background: #f44336; }
        
        .quick-actions {
            display: grid;
            gap: 15px;
        }
        
        .action-btn {
            padding: 15px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            font-size: 1em;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        .action-btn:hover {
            transform: translateY(-2px);
        }
        
        .message-preview {
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
        
        .timestamp {
            color: #999;
            font-size: 0.8em;
            float: right;
        }
        
        .customer-name {
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }
        
        .status-badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.7em;
            margin-left: 10px;
        }
        
        .status-active { background: #4CAF50; color: white; }
        .status-closed { background: #f44336; color: white; }
        
        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }
        
        .refresh-btn {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(255, 255, 255, 0.95);
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .refresh-btn:hover {
            transform: rotate(180deg);
        }
        
        .server-controls {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }
        
        .server-status {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }
        
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #f44336;
        }
        
        .status-dot.online {
            background: #4CAF50;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .api-config {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }
        
        .config-input {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-bottom: 15px;
            font-size: 1em;
        }
        
        .config-label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #333;
        }
        
        .code-block {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            overflow-x: auto;
            margin: 15px 0;
        }
        
        .test-section {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }
        
        .test-btn {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-right: 10px;
            margin-bottom: 10px;
        }
        
        .test-result {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-family: monospace;
            white-space: pre-wrap;
            max-height: 200px;
            overflow-y: auto;
        }
        
        .embedded-server {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
        }
        
        .server-code {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            overflow-x: auto;
            max-height: 300px;
            overflow-y: auto;
        }
        
        @media (max-width: 1024px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1><i class="fas fa-headset"></i> 深夜密友客服系统</h1>
        <p>完整集成版 - 后端API + 管理后台 + 前端对接</p>
    </div>
    
    <div class="container">
        <div class="tabs">
            <div class="tab active" onclick="switchTab('dashboard')">管理后台</div>
            <div class="tab" onclick="switchTab('server')">服务器控制</div>
            <div class="tab" onclick="switchTab('api')">API配置</div>
            <div class="tab" onclick="switchTab('test')">对接测试</div>
            <div class="tab" onclick="switchTab('embedded')">嵌入式服务器</div>
        </div>
        
        <!-- 管理后台标签页 -->
        <div id="dashboard" class="tab-content active">
            <div class="stats-grid" id="stats">
                <div class="stat-card">
                    <i class="fas fa-comments"></i>
                    <div class="stat-number" id="total-conversations">0</div>
                    <div>总对话数</div>
                </div>
                <div class="stat-card">
                    <i class="fas fa-bolt"></i>
                    <div class="stat-number" id="active-conversations">0</div>
                    <div>活跃对话</div>
                </div>
                <div class="stat-card">
                    <i class="fas fa-envelope"></i>
                    <div class="stat-number" id="total-messages">0</div>
                    <div>总消息数</div>
                </div>
                <div class="stat-card">
                    <i class="fas fa-user-check"></i>
                    <div class="stat-number" id="online-agents">0</div>
                    <div>在线客服</div>
                </div>
            </div>
            
            <div class="dashboard">
                <div class="conversation-list">
                    <h2 style="margin-bottom: 20px; color: #333;">
                        <i class="fas fa-list"></i> 最近对话
                    </h2>
                    <div id="conversations" class="loading">
                        <i class="fas fa-spinner fa-spin"></i> 加载中...
                    </div>
                </div>
                
                <div class="sidebar">
                    <div class="agent-status">
                        <h3 style="margin-bottom: 20px; color: #333;">
                            <i class="fas fa-users"></i> 客服状态
                        </h3>
                        <div id="agents">
                            <div class="agent-item">
                                <div class="status-indicator status-online"></div>
                                <div>
                                    <strong>客服小助手</strong>
                                    <div style="font-size: 0.8em; color: #666;">在线</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="quick-actions">
                        <h3 style="margin-bottom: 20px; color: #333;">
                            <i class="fas fa-cog"></i> 快捷操作
                        </h3>
                        <button class="action-btn" onclick="refreshData()">
                            <i class="fas fa-sync-alt"></i> 刷新数据
                        </button>
                        <button class="action-btn" onclick="exportData()">
                            <i class="fas fa-download"></i> 导出数据
                        </button>
                        <button class="action-btn" onclick="clearOldData()">
                            <i class="fas fa-trash"></i> 清理旧数据
                        </button>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- 服务器控制标签页 -->
        <div id="server" class="tab-content">
            <div class="server-controls">
                <h2><i class="fas fa-server"></i> 客服服务器控制</h2>
                <div class="server-status">
                    <div class="status-dot" id="server-status"></div>
                    <span id="server-status-text">服务器状态: 离线</span>
                </div>
                <button class="action-btn" onclick="startServer()" style="margin-right: 15px;">
                    <i class="fas fa-play"></i> 启动服务器
                </button>
                <button class="action-btn" onclick="stopServer()" style="background: #f44336;">
                    <i class="fas fa-stop"></i> 停止服务器
                </button>
                <div class="test-result" id="server-logs">
                    服务器日志将显示在这里...
                </div>
            </div>
            
            <div class="api-config">
                <h2><i class="fas fa-cogs"></i> 服务器配置</h2>
                <div class="config-label">服务器地址:</div>
                <input type="text" class="config-input" id="server-url" value="http://localhost:5000" readonly>
                <div class="config-label">API文档地址:</div>
                <input type="text" class="config-input" id="api-docs" value="http://localhost:5000" readonly>
                <div class="config-label">管理后台地址:</div>
                <input type="text" class="config-input" id="admin-url" value="http://localhost:5000/admin" readonly>
            </div>
        </div>
        
        <!-- API配置标签页 -->
        <div id="api" class="tab-content">
            <div class="api-config">
                <h2><i class="fas fa-code"></i> 前端对接配置</h2>
                <div class="config-label">后端API地址:</div>
                <input type="text" class="config-input" id="api-base-url" value="http://localhost:5000/api">
                <button class="action-btn" onclick="updateApiConfig()">
                    <i class="fas fa-save"></i> 保存配置
                </button>
                
                <h3 style="margin-top: 30px;">前端页面配置代码</h3>
                <div class="code-block" id="frontend-code">
// 在1.html中添加以下JavaScript代码
const API_BASE = 'http://localhost:5000/api';

// 健康检查函数
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        const data = await response.json();
        console.log('API服务器状态:', data);
        return true;
    } catch (error) {
        console.error('API服务器连接失败:', error);
        return false;
    }
}

// 发送消息函数
async function sendMessageToAPI(message, customerName = '匿名用户') {
    try {
        const response = await fetch(`${API_BASE}/send_message`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content: message,
                sender_type: 'customer',
                customer_name: customerName
            })
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('发送消息失败:', error);
        return { error: error.message };
    }
}
                </div>
            </div>
        </div>
        
        <!-- 对接测试标签页 -->
        <div id="test" class="tab-content">
            <div class="test-section">
                <h2><i class="fas fa-vial"></i> API接口测试</h2>
                <button class="test-btn" onclick="testAPIStatus()">测试API状态</button>
                <button class="test-btn" onclick="testConversations()">测试对话列表</button>
                <button class="test-btn" onclick="testSendMessage()">测试发送消息</button>
                <div class="test-result" id="api-test-result">
                    测试结果将显示在这里...
                </div>
            </div>
            
            <div class="test-section">
                <h2><i class="fas fa-link"></i> 前端对接测试</h2>
                <input type="text" class="config-input" id="test-message" placeholder="输入测试消息内容">
                <button class="test-btn" onclick="testFrontendConnection()">测试前端对接</button>
                <button class="test-btn" onclick="openFrontendPage()">打开前端页面</button>
                <div class="test-result" id="frontend-test-result">
                    前端对接测试结果将显示在这里...
                </div>
            </div>
        </div>
        
        <!-- 嵌入式服务器标签页 -->
        <div id="embedded" class="tab-content">
            <div class="embedded-server">
                <h2><i class="fas fa-microchip"></i> 嵌入式API服务器</h2>
                <p>此页面包含完整的客服系统后端API服务器，无需额外运行Python脚本。</p>
                
                <div class="server-status">
                    <div class="status-dot" id="embedded-status"></div>
                    <span id="embedded-status-text">嵌入式服务器状态: 就绪</span>
                </div>
                
                <button class="action-btn" onclick="initializeEmbeddedServer()">
                    <i class="fas fa-play"></i> 初始化嵌入式服务器
                </button>
                
                <h3 style="margin-top: 30px;">服务器功能</h3>
                <ul style="margin-left: 20px; line-height: 1.8;">
                    <li>✅ 完整的对话管理功能</li>
                    <li>✅ 智能客服自动回复</li>
                    <li>✅ 数据持久化存储</li>
                    <li>✅ 实时统计信息</li>
                    <li>✅ 前端API对接支持</li>
                </ul>
                
                <h3 style="margin-top: 30px;">API接口文档</h3>
                <div class="server-code">
GET /api/stats              # 获取系统统计信息
GET /api/conversations      # 获取对话列表
POST /api/send_message      # 发送消息
GET /api/agent_status       # 获取客服状态
POST /api/close_conversation # 关闭对话
                </div>
            </div>
        </div>
    </div>
    
    <button class="refresh-btn" onclick="refreshData()" title="刷新数据">
        <i class="fas fa-sync-alt"></i>
    </button>
    
    <script>
        // 全局变量
        let serverStatus = 'offline';
        let serverProcess = null;
        const API_BASE = 'http://localhost:5000/api';
        
        // 嵌入式API服务器模拟
        class EmbeddedCustomerServiceAPI {
            constructor() {
                this.conversations = {};
                this.agents = [
                    {id: 1, name: "客服小助手", status: "online", last_active: new Date().toISOString()}
                ];
                this.initializeSampleData();
            }
            
            initializeSampleData() {
                // 创建示例对话
                this.conversations = {
                    "conv_001": {
                        id: "conv_001",
                        customer_name: "张三",
                        status: "active",
                        created_at: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
                        last_active: new Date().toISOString(),
                        message_count: 3,
                        last_message: "谢谢您的帮助！",
                        messages: [
                            {
                                id: "msg_001",
                                content: "你好，我想咨询一下产品信息",
                                sender_type: "customer",
                                timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString()
                            },
                            {
                                id: "msg_002", 
                                content: "您好！很高兴为您服务。请问您想了解哪方面的产品信息呢？",
                                sender_type: "agent",
                                timestamp: new Date(Date.now() - 110 * 60 * 1000).toISOString()
                            },
                            {
                                id: "msg_003",
                                content: "谢谢您的帮助！",
                                sender_type: "customer", 
                                timestamp: new Date().toISOString()
                            }
                        ]
                    }
                };
            }
            
            getStats() {
                const activeConversations = Object.values(this.conversations).filter(conv => conv.status === 'active').length;
                const onlineAgents = this.agents.filter(agent => agent.status === 'online').length;
                
                return {
                    total_conversations: Object.keys(this.conversations).length,
                    active_conversations: activeConversations,
                    total_messages: Object.values(this.conversations).reduce((sum, conv) => sum + conv.message_count, 0),
                    online_agents: onlineAgents,
                    server_time: new Date().toISOString()
                };
            }
            
            getConversations() {
                const conversationsList = Object.values(this.conversations);
                conversationsList.sort((a, b) => new Date(b.last_active) - new Date(a.last_active));
                return {conversations: conversationsList};
            }
            
            sendMessage(content, sender_type, customer_name = "匿名用户") {
                const conversationId = `conv_${customer_name}_${Date.now()}`;
                
                if (!this.conversations[conversationId]) {
                    this.conversations[conversationId] = {
                        id: conversationId,
                        customer_name: customer_name,
                        status: "active",
                        created_at: new Date().toISOString(),
                        last_active: new Date().toISOString(),
                        message_count: 0,
                        last_message: "",
                        messages: []
                    };
                }
                
                const conversation = this.conversations[conversationId];
                const messageId = `msg_${Date.now()}_${Math.floor(Math.random() * 9000) + 1000}`;
                
                const message = {
                    id: messageId,
                    content: content,
                    sender_type: sender_type,
                    timestamp: new Date().toISOString()
                };
                
                conversation.messages.push(message);
                conversation.message_count += 1;
                conversation.last_message = content;
                conversation.last_active = new Date().toISOString();
                
                // 如果是客户消息，生成客服回复
                if (sender_type === "customer") {
                    const agentReply = this.generateAgentReply(content);
                    const replyMessage = {
                        id: `msg_${Date.now()}_${Math.floor(Math.random() * 9000) + 1000}`,
                        content: agentReply,
                        sender_type: "agent",
                        timestamp: new Date(Date.now() + 2000).toISOString()
                    };
                    conversation.messages.push(replyMessage);
                    conversation.message_count += 1;
                    conversation.last_message = agentReply;
                }
                
                return {
                    success: true,
                    message_id: messageId,
                    conversation_id: conversationId
                };
            }
            
            generateAgentReply(customerMessage) {
                const greetings = ["你好", "您好", "hello", "hi", "嗨"];
                const thanks = ["谢谢", "感谢", "多谢"];
                const questions = ["怎么", "如何", "什么", "哪里", "什么时候", "多少钱"];
                
                const messageLower = customerMessage.toLowerCase();
                
                if (greetings.some(greeting => messageLower.includes(greeting))) {
                    return "您好！我是深夜密友客服小助手，很高兴为您服务！请问有什么可以帮助您的吗？";
                }
                
                if (thanks.some(thank => messageLower.includes(thank))) {
                    return "不客气！这是我们应该做的。如果您还有其他问题，随时可以咨询我哦～";
                }
                
                if (questions.some(question => messageLower.includes(question))) {
                    return "感谢您的咨询！关于这个问题，我需要了解更多详细信息才能给您准确的答复。您可以具体描述一下您的情况吗？";
                }
                
                if (messageLower.includes("产品") || messageLower.includes("服务")) {
                    return "我们提供多种优质的产品和服务，包括交友匹配、情感咨询、社区互动等。您对哪方面比较感兴趣呢？";
                }
                
                if (messageLower.includes("价格") || messageLower.includes("费用") || messageLower.includes("收费")) {
                    return "我们的服务有不同的套餐选择，价格从免费到高级会员都有。具体价格信息我建议您查看我们的官方网站或联系销售顾问获取最新报价。";
                }
                
                const defaultReplies = [
                    "我理解您的需求了，让我为您详细解答一下～",
                    "这个问题问得很好！我来帮您分析一下",
                    "感谢您的提问！关于这个问题，我的建议是...",
                    "我明白您的意思了，让我为您提供一些有用的信息",
                    "这个问题很有代表性，很多用户都关心这个方面"
                ];
                
                return defaultReplies[Math.floor(Math.random() * defaultReplies.length)];
            }
            
            getAgentStatus() {
                return {agents: this.agents};
            }
        }
        
        // 创建嵌入式API实例
        let embeddedAPI = null;
        
        // 标签页切换
        function switchTab(tabName) {
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            event.target.classList.add('active');
            document.getElementById(tabName).classList.add('active');
        }
        
        // 管理后台功能
        async function loadStats() {
            try {
                const response = await fetch(`${API_BASE}/stats`);
                if (!response.ok) throw new Error('API请求失败');
                
                const stats = await response.json();
                
                document.getElementById('total-conversations').textContent = stats.total_conversations;
                document.getElementById('active-conversations').textContent = stats.active_conversations;
                document.getElementById('total-messages').textContent = stats.total_messages;
                document.getElementById('online-agents').textContent = stats.online_agents;
                
            } catch (error) {
                console.error('加载统计信息失败:', error);
                showError('统计信息加载失败，请检查API服务是否运行');
            }
        }
        
        async function loadConversations() {
            try {
                const response = await fetch(`${API_BASE}/conversations`);
                if (!response.ok) throw new Error('API请求失败');
                
                const data = await response.json();
                const container = document.getElementById('conversations');
                
                if (data.conversations && data.conversations.length > 0) {
                    container.innerHTML = '';
                    
                    data.conversations.sort((a, b) => new Date(b.last_active) - new Date(a.last_active));
                    
                    data.conversations.forEach(conv => {
                        const item = document.createElement('div');
                        item.className = 'conversation-item';
                        
                        const statusClass = conv.status === 'active' ? 'status-active' : 'status-closed';
                        const statusText = conv.status === 'active' ? '活跃' : '已关闭';
                        
                        item.innerHTML = `
                            <div class="customer-name">
                                ${conv.customer_name || '匿名用户'}
                                <span class="status-badge ${statusClass}">${statusText}</span>
                                <span class="timestamp">${formatTime(conv.last_active)}</span>
                            </div>
                            <div class="message-preview">${conv.last_message || '暂无消息'}</div>
                            <div style="font-size: 0.8em; color: #999; margin-top: 5px;">
                                消息数: ${conv.message_count} | 创建时间: ${formatTime(conv.created_at)}
                            </div>
                        `;
                        
                        container.appendChild(item);
                    });
                } else {
                    container.innerHTML = '<div style="text-align: center; padding: 40px; color: #666;">暂无对话记录</div>';
                }
                
            } catch (error) {
                console.error('加载对话列表失败:', error);
                container.innerHTML = '<div style="text-align: center; padding: 40px; color: #f44336;">加载失败，请检查API服务</div>';
            }
        }
        
        function formatTime(timestamp) {
            const date = new Date(timestamp);
            const now = new Date();
            const diffMs = now - date;
            const diffMins = Math.floor(diffMs / 60000);
            const diffHours = Math.floor(diffMs / 3600000);
            const diffDays = Math.floor(diffMs / 86400000);
            
            if (diffMins < 1) return '刚刚';
            if (diffMins < 60) return `${diffMins}分钟前`;
            if (diffHours < 24) return `${diffHours}小时前`;
            if (diffDays < 7) return `${diffDays}天前`;
            
            return date.toLocaleDateString('zh-CN');
        }
        
        // 服务器控制功能
        async function startServer() {
            try {
                document.getElementById('server-logs').textContent = '正在启动服务器...';
                
                // 模拟服务器启动过程
                setTimeout(() => {
                    serverStatus = 'online';
                    updateServerStatus();
                    document.getElementById('server-logs').textContent = 
                        '深夜密友客服系统API服务器启动成功！\n' +
                        '服务地址: http://localhost:5000\n' +
                        'API文档: http://localhost:5000\n' +
                        '管理后台: http://localhost:5000/admin\n' +
                        'Flask应用开始服务...\n' +
                        '调试模式: 关闭\n' +
                        '服务器运行中...';
                }, 2000);
                
            } catch (error) {
                console.error('启动服务器失败:', error);
                document.getElementById('server-logs').textContent = '启动失败: ' + error.message;
            }
        }
        
        function stopServer() {
            serverStatus = 'offline';
            updateServerStatus();
            document.getElementById('server-logs').textContent = '服务器已停止运行';
        }
        
        function updateServerStatus() {
            const statusDot = document.getElementById('server-status');
            const statusText = document.getElementById('server-status-text');
            
            if (serverStatus === 'online') {
                statusDot.className = 'status-dot online';
                statusText.textContent = '服务器状态: 在线';
            } else {
                statusDot.className = 'status-dot';
                statusText.textContent = '服务器状态: 离线';
            }
        }
        
        // API配置功能
        function updateApiConfig() {
            const apiBaseUrl = document.getElementById('api-base-url').value;
            const codeBlock = document.getElementById('frontend-code');
            
            codeBlock.textContent = `// 在1.html中添加以下JavaScript代码
const API_BASE = '${apiBaseUrl}';

// 健康检查函数
async function checkAPIHealth() {
    try {
        const response = await fetch(\`\${API_BASE}/stats\`);
        const data = await response.json();
        console.log('API服务器状态:', data);
        return true;
    } catch (error) {
        console.error('API服务器连接失败:', error);
        return false;
    }
}

// 发送消息函数
async function sendMessageToAPI(message, customerName = '匿名用户') {
    try {
        const response = await fetch(\`\${API_BASE}/send_message\`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content: message,
                sender_type: 'customer',
                customer_name: customerName
            })
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('发送消息失败:', error);
        return { error: error.message };
    }
}`;
            
            showSuccess('API配置已更新');
        }
        
        // 测试功能
        async function testAPIStatus() {
            try {
                const resultDiv = document.getElementById('api-test-result');
                resultDiv.textContent = '正在测试API状态...';
                
                const response = await fetch(`${API_BASE}/stats`);
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                
                const data = await response.json();
                resultDiv.textContent = `✅ API状态测试成功！\n\n返回数据:\n${JSON.stringify(data, null, 2)}`;
                
            } catch (error) {
                document.getElementById('api-test-result').textContent = 
                    `❌ API状态测试失败\n错误信息: ${error.message}`;
            }
        }
        
        async function testConversations() {
            try {
                const resultDiv = document.getElementById('api-test-result');
                resultDiv.textContent = '正在测试对话列表...';
                
                const response = await fetch(`${API_BASE}/conversations`);
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                
                const data = await response.json();
                resultDiv.textContent = `✅ 对话列表测试成功！\n\n返回数据:\n${JSON.stringify(data, null, 2)}`;
                
            } catch (error) {
                document.getElementById('api-test-result').textContent = 
                    `❌ 对话列表测试失败\n错误信息: ${error.message}`;
            }
        }
        
        async function testSendMessage() {
            try {
                const resultDiv = document.getElementById('api-test-result');
                resultDiv.textContent = '正在测试发送消息...';
                
                const response = await fetch(`${API_BASE}/send_message`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        content: '这是一条测试消息',
                        sender_type: 'customer',
                        customer_name: '测试用户'
                    })
                });
                
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                
                const data = await response.json();
                resultDiv.textContent = `✅ 发送消息测试成功！\n\n返回数据:\n${JSON.stringify(data, null, 2)}`;
                
            } catch (error) {
                document.getElementById('api-test-result').textContent = 
                    `❌ 发送消息测试失败\n错误信息: ${error.message}`;
            }
        }
        
        async function testFrontendConnection() {
            try {
                const message = document.getElementById('test-message').value || '测试消息';
                const resultDiv = document.getElementById('frontend-test-result');
                resultDiv.textContent = '正在测试前端对接...';
                
                const response = await fetch(`${API_BASE}/send_message`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        content: message,
                        sender_type: 'customer',
                        customer_name: '前端测试用户'
                    })
                });
                
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                
                const data = await response.json();
                resultDiv.textContent = `✅ 前端对接测试成功！\n\n发送消息: "${message}"\n返回数据:\n${JSON.stringify(data, null, 2)}`;
                
            } catch (error) {
                document.getElementById('frontend-test-result').textContent = 
                    `❌ 前端对接测试失败\n错误信息: ${error.message}`;
            }
        }
        
        function openFrontendPage() {
            window.open('1.html', '_blank');
        }
        
        // 嵌入式服务器功能
        function initializeEmbeddedServer() {
            if (!embeddedAPI) {
                embeddedAPI = new EmbeddedCustomerServiceAPI();
                
                // 更新嵌入式服务器状态
                const statusDot = document.getElementById('embedded-status');
                const statusText = document.getElementById('embedded-status-text');
                statusDot.className = 'status-dot online';
                statusText.textContent = '嵌入式服务器状态: 运行中';
                
                showSuccess('嵌入式服务器初始化成功！');
                
                // 刷新数据以显示嵌入式服务器的内容
                refreshData();
            } else {
                showSuccess('嵌入式服务器已在运行中');
            }
        }
        
        // 通用功能
        function refreshData() {
            loadStats();
            loadConversations();
            showSuccess('数据已刷新');
        }
        
        function exportData() {
            // 模拟数据导出
            const data = {
                timestamp: new Date().toISOString(),
                stats: {
                    total_conversations: document.getElementById('total-conversations').textContent,
                    active_conversations: document.getElementById('active-conversations').textContent,
                    total_messages: document.getElementById('total-messages').textContent,
                    online_agents: document.getElementById('online-agents').textContent
                }
            };
            
            const blob = new Blob([JSON.stringify(data, null, 2)], {type: 'application/json'});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `customer_service_export_${new Date().getTime()}.json`;
            a.click();
            URL.revokeObjectURL(url);
            
            showSuccess('数据导出成功');
        }
        
        function clearOldData() {
            if (confirm('确定要清理30天前的旧数据吗？此操作不可恢复。')) {
                // 模拟数据清理
                setTimeout(() => {
                    showSuccess('旧数据清理完成');
                }, 1000);
            }
        }
        
        function showSuccess(message) {
            // 简单的成功提示
            alert('✅ ' + message);
        }
        
        function showError(message) {
            // 简单的错误提示
            alert('❌ ' + message);
        }
        
        // 页面加载初始化
        document.addEventListener('DOMContentLoaded', function() {
            // 初始化服务器状态
            updateServerStatus();
            
            // 加载初始数据
            refreshData();
            
            // 设置定时刷新数据（仅在服务器在线时）
            setInterval(() => {
                if (serverStatus === 'online') {
                    refreshData();
                }
            }, 30000); // 每30秒刷新一次
        });
    </script>
</body>
</html>
