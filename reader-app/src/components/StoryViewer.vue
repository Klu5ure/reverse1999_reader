<template>
    <div class="story-viewer">
      <div class="story-header">
        <h2>{{ formatTitle(file.name) }}</h2>
        <button class="language-toggle" @click="toggleLanguage">
          {{ language === 'chinese' ? '切换到英文' : '切换到中文' }}
        </button>
      </div>
      
      <div v-if="loading" class="loading">
        加载中...
      </div>
      
      <div v-else-if="error" class="error">
        加载失败: {{ error }}
      </div>
      
      <div v-else class="story-content">
        <div v-for="(dialog, index) in storyContent" :key="index" class="dialog">
          <div class="dialog-content">
            <span class="speaker">{{ dialog[`${language}_speaker`] }}</span>
            <span 
              class="text clickable" 
              @click="toggleDialogTranslation(index)"
            >
              {{ dialog[`${language}_text`] }}
            </span>
          </div>
          <div 
            v-if="expandedDialogs[index]" 
            class="translation"
          >
            <div class="dialog-content">
              <span class="speaker">{{ formatSpeaker(dialog[`${language === 'chinese' ? 'english' : 'chinese'}_speaker`]) }}</span>
              <span class="translation-text">{{ dialog[`${language === 'chinese' ? 'english' : 'chinese'}_text`] }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'StoryViewer',
    props: {
      file: {
        type: Object,
        required: true
      },
      language: {
        type: String,
        default: 'chinese'
      }
    },
    data() {
      return {
        storyContent: [],
        loading: true,
        error: null,
        expandedDialogs: {} // 用于跟踪哪些对话框已展开
      };
    },
    watch: {
      file: {
        immediate: true,
        handler() {
          this.loadStoryContent();
          this.expandedDialogs = {}; // 重置展开状态
        }
      }
    },
    methods: {
      async loadStoryContent() {
        this.loading = true;
        this.error = null;
        
        try {
          // 在实际开发中，你需要创建一个后端服务来提供这些数据
          // 这里我们假设有一个API可以获取文件内容
          const response = await axios.get(`/api/files/${encodeURIComponent(this.file.path)}`);
          this.storyContent = response.data;
          this.loading = false;
        } catch (error) {
          console.error('加载故事内容失败:', error);
          this.error = '无法加载故事内容，请稍后再试';
          this.loading = false;
          
          // 为了演示，我们可以使用模拟数据
          setTimeout(() => {
            this.storyContent = [
              {
                "chinese_speaker": "小叶尼塞：",
                "chinese_text": "——放开我！你带我去哪儿？！",
                "english_speaker": "Yenisei",
                "english_text": "Let me go! Where are you taking me?!"
              },
              {
                "chinese_speaker": "小叶尼塞：",
                "chinese_text": "你——",
                "english_speaker": "Yenisei",
                "english_text": "You ..."
              },
              {
                "chinese_speaker": "？？？：",
                "chinese_text": "我现下放开，你摔落便是死路一条。",
                "english_speaker": "???",
                "english_text": "If I let go, you will fall, and death will be your end."
              }
            ];
            this.error = null;
            this.loading = false;
          }, 1000);
        }
      },
      formatTitle(name) {
        return name.replace(/\.json$/, '');
      },
      
      formatSpeaker(speaker) {
        // 确保说话者名称后面有冒号或空格
        if (!speaker) return '';
        if (speaker.endsWith(':') || speaker.endsWith('：')) {
          return speaker;
        }
        // 根据语言添加适当的冒号
        return speaker + (speaker.match(/[a-zA-Z]/) ? ': ' : '：');
      },
      
      toggleLanguage() {
        this.$emit('toggle-language');
        this.expandedDialogs = {}; // 切换语言时重置展开状态
      },
      toggleDialogTranslation(index) {
        // 切换特定对话的展开状态
        this.expandedDialogs[index] = !this.expandedDialogs[index];
        // 强制更新视图
        this.$forceUpdate();
      }
    }
  }
  </script>
  
  <style scoped>
  .story-viewer {
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  
  .story-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #e0e0e0;
  }
  
  .language-toggle {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 8px 16px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .language-toggle:hover {
    background-color: #45a049;
  }
  
  .loading, .error {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    color: #888;
  }
  
  .error {
    color: #f44336;
  }
  
  .story-content {
    flex: 1;
    overflow-y: auto;
  }
  
  .dialog {
    margin-bottom: 20px;
    animation: fadeIn 0.5s;
  }
  
  .dialog-content {
    display: flex;
    align-items: baseline; /* 改为baseline对齐 */
  }
  
  .speaker {
    font-weight: bold;
    color: #2196F3;
    margin-right: 5px;
    white-space: nowrap;
    line-height: 1.6; /* 与文本保持相同的行高 */
  }
  
  .text {
    line-height: 1.6;
    white-space: pre-wrap;
    flex: 1;
  }
  
  .translation-text {
    line-height: 1.6;
    white-space: pre-wrap;
    flex: 1;
  }
  
  .clickable {
    cursor: pointer;
    padding: 5px;
    border-radius: 4px;
    transition: background-color 0.2s;
  }
  
  .clickable:hover {
    background-color: #f5f5f5;
  }
  
  .translation {
    margin-top: 8px;
    padding: 10px;
    background-color: #f9f9f9;
    border-left: 3px solid #2196F3;
    border-radius: 0 4px 4px 0;
    animation: slideDown 0.3s;
  }
  
  .translation-header {
    font-weight: bold;
    margin-bottom: 5px;
    color: #757575;
    font-size: 0.9em;
  }
  
  .translation-text {
    line-height: 1.6;
    white-space: pre-wrap;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  
  @keyframes slideDown {
    from { 
      opacity: 0;
      transform: translateY(-10px);
    }
    to { 
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @media (max-width: 768px) {
    .story-header {
      flex-direction: column;
      align-items: flex-start;
    }
    
    .language-toggle {
      margin-top: 10px;
      align-self: flex-end;
    }
    
    .dialog {
      padding: 10px 5px;
    }
    
    .clickable {
      padding: 8px 5px; /* 增加可点击区域 */
    }
  }
  </style>