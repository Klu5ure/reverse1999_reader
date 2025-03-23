from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)  # 启用CORS，允许前端访问

# 基础路径
BASE_PATH = r"d:\errorhassei\project\reverse_front"
SIDE_STORY_PATH = os.path.join(BASE_PATH, "side_story")

@app.route('/api/files', methods=['GET'])
def get_files():
    """获取文件结构"""
    try:
        notes_path = os.path.join(SIDE_STORY_PATH, "Notes on Shuori")
        if not os.path.exists(notes_path):
            return jsonify({"error": "目录不存在"}), 404
        
        files = [f for f in os.listdir(notes_path) if f.endswith('.json')]
        
        file_structure = [
            {
                "name": "Notes on Shuori",
                "type": "directory",
                "children": [
                    {
                        "name": file,
                        "type": "file",
                        "path": f"side_story/Notes on Shuori/{file}"
                    } for file in files
                ]
            }
        ]
        
        return jsonify(file_structure)
    except Exception as e:
        return jsonify({"error": f"获取文件结构失败: {str(e)}"}), 500

@app.route('/api/files/<path:file_path>', methods=['GET'])
def get_file_content(file_path):
    """获取文件内容"""
    try:
        full_path = os.path.join(BASE_PATH, file_path)
        if not os.path.exists(full_path):
            return jsonify({"error": "文件不存在"}), 404
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
        
        return jsonify(content)
    except Exception as e:
        return jsonify({"error": f"获取文件内容失败: {str(e)}"}), 500

# 在文件末尾的 if __name__ == '__main__': 部分修改为
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)