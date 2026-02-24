# GitHub上传指南

## 方法一：通过GitHub网页上传（推荐，简单）

1. 登录 https://github.com
2. 点击右上角 "+" → "New repository"
3. 填写仓库信息：
   - Repository name: `sost-tnbc-figures` (或其他名称)
   - Description: `Code and data for SOST analysis figures in TNBC research`
   - 选择 Public 或 Private
   - 不勾选 "Add a README file"（我们已经有了）
4. 创建仓库后，点击 "uploading an existing file"
5. 将 `github/` 文件夹内的所有内容拖拽上传

## 方法二：通过命令行上传

### 步骤1: 初始化Git仓库
```bash
cd /WorkspaceP1/yangx/sost_tnbc/github
git init
git add .
git commit -m "Initial commit: SOST TNBC analysis figures"
```

### 步骤2: 关联GitHub远程仓库
在GitHub网站创建新仓库后，复制仓库URL，然后：
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## 方法三：使用GitHub Desktop（最简单）

1. 下载安装 GitHub Desktop
2. File → Add Local Repository → 选择 `/WorkspaceP1/yangx/sost_tnbc/github`
3. Commit 并 Push

## 文件检查清单

确保以下文件都在 `github/` 文件夹中：

- [x] data/TNBC_HER2_Luminal-SOST.xlsx
- [x] data/SOST_MKI67_Unique_Samples.csv
- [x] figures/figure1_hscore_distribution.png
- [x] figures/figure2_sost_mki67_correlation.png
- [x] scripts/figure1_hscore_distribution.py
- [x] scripts/figure2_sost_mki67_correlation.py
- [x] README.md
- [x] FILE_CORRESPONDENCE.md

## 建议的仓库设置

- **License**: MIT License（或根据期刊要求选择）
- **.gitignore**: 添加Python忽略规则
- **Topics**: sost, tnbc, breast-cancer, gene-expression, biomarker

## 上传后

仓库URL可以用于：
- 论文补充材料
- 审稿人数据验证
- 代码共享引用
