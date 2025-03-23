<template>
    <div class="directory-tree">
      <ul>
        <li v-for="(item, index) in files" :key="index">
          <div 
            v-if="item.type === 'directory'" 
            class="directory"
            @click="toggleDirectory(item)"
          >
            <span class="icon">{{ item.expanded ? '▼' : '▶' }}</span>
            <span class="name">{{ item.name }}</span>
          </div>
          <div 
            v-else 
            class="file"
            :class="{ active: isActive(item) }"
            @click="selectFile(item)"
          >
            <span class="icon">•</span>
            <span class="name">{{ formatFileName(item.name) }}</span>
          </div>
          
          <directory-tree 
            v-if="item.type === 'directory' && item.expanded" 
            :files="item.children" 
            @select-file="onSelectFile"
            class="nested"
          />
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DirectoryTree',
    props: {
      files: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        selectedFile: null
      };
    },
    methods: {
      toggleDirectory(directory) {
        directory.expanded = !directory.expanded;
      },
      selectFile(file) {
        this.selectedFile = file;
        this.$emit('select-file', file);
      },
      onSelectFile(file) {
        this.selectedFile = file;
        this.$emit('select-file', file);
      },
      isActive(file) {
        return this.selectedFile === file;
      },
      formatFileName(name) {
        return name.replace(/\.json$/, '');
      }
    },
    created() {
      this.files.forEach(item => {
        if (item.type === 'directory') {
          item.expanded = true;
        }
      });
    }
  }
  </script>
  
  <style scoped>
  .directory-tree {
    user-select: none;
  }
  
  .directory-tree ul {
    list-style-type: none;
    padding-left: 0;
    margin: 0;
  }
  
  .nested {
    margin-left: 20px; /* 子目录缩进 */
  }
  
  .directory, .file {
    padding: 5px;
    cursor: pointer;
    display: flex;
    align-items: center;
    border-radius: 4px;
    margin-bottom: 2px;
  }
  
  .directory:hover, .file:hover {
    background-color: #e9e9e9;
  }
  
  .file.active {
    background-color: #d1e8ff;
    font-weight: bold;
  }
  
  .icon {
    margin-right: 8px;
    font-size: 16px; /* 增大图标尺寸，便于在移动设备上点击 */
    width: 20px;
    text-align: center;
    color: #666;
  }
  
  .directory .icon {
    color: #2196F3;
  }
  
  .name {
    flex: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  @media (max-width: 768px) {
    .directory, .file {
      padding: 10px 5px; /* 增加垂直内边距，便于触摸 */
    }
    
    .nested {
      margin-left: 15px; /* 在小屏幕上减少缩进 */
    }
  }
  </style>