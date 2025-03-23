<template>
  <div id="app">
    <div class="container">
      <div class="sidebar" :class="{ 'collapsed': sidebarCollapsed }">
        <div class="sidebar-header">
          <h2 v-if="!sidebarCollapsed">故事目录</h2>
          <button class="toggle-sidebar" @click="toggleSidebar">
            {{ sidebarCollapsed ? '»' : '«' }}
          </button>
        </div>
        <directory-tree v-if="!sidebarCollapsed" :files="files" @select-file="selectFile" />
      </div>
      <div class="content">
        <story-viewer 
          v-if="selectedFile" 
          :file="selectedFile" 
          :language="language" 
          @toggle-language="toggleLanguage" 
        />
        <div v-else class="welcome">
          <h2>欢迎使用故事阅读器</h2>
          <p>请从左侧选择一个故事开始阅读</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import DirectoryTree from './components/DirectoryTree.vue';
import StoryViewer from './components/StoryViewer.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    DirectoryTree,
    StoryViewer
  },
  data() {
    return {
      files: [],
      selectedFile: null,
      language: 'chinese', // 默认显示中文
      sidebarCollapsed: false // 侧边栏折叠状态
    };
  },
  mounted() {
    this.loadFileStructure();
  },
  methods: {
    async loadFileStructure() {
      try {
        // 这里需要替换为你的API端点，用于获取文件结构
        // 在实际开发中，你需要创建一个后端服务来提供这些数据
        // 这里我们假设有一个API可以获取文件结构
        const response = await axios.get('/api/files');
        this.files = response.data;
      } catch (error) {
        console.error('加载文件结构失败:', error);
        // 为了演示，我们可以使用硬编码的文件结构
        this.files = [
          {
            name: 'Notes on Shuori',
            type: 'directory',
            children: [
              { name: 'NS-01 启程的祷声.json', type: 'file', path: 'side_story/Notes on Shuori/NS-01 启程的祷声.json' },
              { name: 'NS-03 仙子草地.json', type: 'file', path: 'side_story/Notes on Shuori/NS-03 仙子草地.json' },
              { name: 'NS-04 俯身旷野.json', type: 'file', path: 'side_story/Notes on Shuori/NS-04 俯身旷野.json' },
              { name: 'NS-08 十万个问答.json', type: 'file', path: 'side_story/Notes on Shuori/NS-08 十万个问答.json' },
              { name: 'NS-10 异乡人关怀.json', type: 'file', path: 'side_story/Notes on Shuori/NS-10 异乡人关怀.json' },
              { name: 'NS-14 往日鎏金.json', type: 'file', path: 'side_story/Notes on Shuori/NS-14 往日鎏金.json' },
              { name: 'NS-15 空心眼.json', type: 'file', path: 'side_story/Notes on Shuori/NS-15 空心眼.json' },
              { name: 'NS-16 见我所见.json', type: 'file', path: 'side_story/Notes on Shuori/NS-16 见我所见.json' },
              { name: 'NS-19 hopefully.json', type: 'file', path: 'side_story/Notes on Shuori/NS-19 hopefully.json' },
              { name: 'NS-20 别春山.json', type: 'file', path: 'side_story/Notes on Shuori/NS-20 别春山.json' },
              { name: 'NS-22 "所求必应".json', type: 'file', path: 'side_story/Notes on Shuori/NS-22 "所求必应".json' },
              { name: 'NS-23 他日再逢.json', type: 'file', path: 'side_story/Notes on Shuori/NS-23 他日再逢.json' },
            ]
          }
        ];
      }
    },
    selectFile(file) {
      this.selectedFile = file;
    },
    toggleLanguage() {
      this.language = this.language === 'chinese' ? 'english' : 'chinese';
    },
    toggleSidebar() {
      this.sidebarCollapsed = !this.sidebarCollapsed;
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100vh;
  margin: 0;
  padding: 0;
}

.container {
  display: flex;
  height: 100%;
  flex-direction: column; /* 默认为上下布局，适合移动设备 */
}

.sidebar {
  width: 100%;
  background-color: #f5f5f5;
  padding: 10px;
  overflow-y: auto;
  border-bottom: 1px solid #e0e0e0;
  transition: max-height 0.3s;
  max-height: 300px;
}

.sidebar.collapsed {
  max-height: 50px;
  padding: 5px 10px;
}

.sidebar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.toggle-sidebar {
  background: none;
  border: none;
  font-size: 18px;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 4px;
  color: #666;
}

.toggle-sidebar:hover {
  background-color: #e0e0e0;
}

.content {
  flex: 1;
  padding: 15px;
  overflow-y: auto;
}

.welcome {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #888;
}

h2 {
  margin-top: 0;
  margin-bottom: 15px;
  color: #333;
}

/* 桌面端样式 */
@media (min-width: 769px) {
  .container {
    flex-direction: row; /* 桌面端使用左右布局 */
  }
  
  .sidebar {
    width: 300px;
    height: 100%;
    max-height: none;
    border-bottom: none;
    border-right: 1px solid #e0e0e0;
    padding: 20px;
  }
  
  .sidebar.collapsed {
    width: 40px;
    max-height: none;
    padding: 10px;
  }
}
</style>