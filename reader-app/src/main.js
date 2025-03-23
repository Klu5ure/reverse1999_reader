import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

// 配置axios基础URL - 使用相对路径或完整URL
// 在移动设备上，需要确保使用正确的服务器地址
const isDevelopment = process.env.NODE_ENV === 'development';
axios.defaults.baseURL = isDevelopment 
  ? window.location.origin  // 使用当前页面的源
  : 'http://localhost:3000'; // 或者你的生产环境API地址

// 添加超时设置
axios.defaults.timeout = 10000; // 10秒

// 添加错误处理拦截器
axios.interceptors.response.use(
  response => response,
  error => {
    console.error('API请求失败:', error);
    if (error.code === 'ECONNABORTED') {
      console.error('请求超时');
    }
    return Promise.reject(error);
  }
);

createApp(App).mount('#app')