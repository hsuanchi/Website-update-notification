# Article Collection

## 一. 介紹

### 1. 計畫說明：

想法主要是來自 [Feedly](https://feedly.com/i/welcome) 這個網站，feed 是被餵食的概念，但他沒辦法追蹤到所有想追的網站，於是開始寫了這個 Side project，希望這專案能讓自己更留意平時被餵食的資訊，並利用串接 LineBot 後即時獲得重要資訊

### 2. 功能：


可以瀏覽六大類型 (Google Official Blog、GTM Blog、SEO Blog、Google Analytics、FB Blog、E-Shop) 的文章內容，有各自的 RSS 訂閱，和 LineBot 即時更新通知群組

![image](https://github.com/hsuanchi/Website-update-notification/blob/master/img/article.png)

後台 (ReadOnly)：https://article.maxlist.xyz/admin

可以確認目前爬蟲健康狀態，在網頁上新增爬蟲任務、修改目前爬蟲設定的 CSS 節點、刪除不需要的爬蟲任務，和 Restart 單隻爬蟲或多隻爬蟲

![image](https://github.com/hsuanchi/Website-update-notification/blob/master/img/article_admin.png)

## 二. 進度

### week1 進度：爬蟲框架
- [x] 新增 - 爬蟲的控制模組完成
- [x] 新增 - 資料庫串接

![image](https://github.com/hsuanchi/Website-update-notification/blob/master/img/article_collection.png)

### week2 進度：前後台頁面
- [x] 新增 Home Page - 文章列表
- [x] 新增 Admin Page - 目前爬蟲狀態
- [x] 新增 All Page - Ｍenu Bar
- [x] 新增 All Page - Login Page
- [x] 新增 Admin Page - 新增爬蟲
- [x] 新增 Admin Page - 修改爬蟲
- [x] 新增 Admin Page - 刪除爬蟲
- [x] 新增 Admin Page - Restart
- [x] 新增 Admin Page - Read Only 的 Admin page
- [x] 新增 - GCE 部署 (CentOS7 + Apache + Flask)
- [x] 新增 - Hostname 處理
- [x] 新增 - Crontab 爬蟲定時處理
 
### week3 進度：新增 LineBot 通知
- [x] 新增：有新文章更新時 Line bot 通知(使用 RSS + ifttt )
- [x] 調整：爬蟲時間錯亂 (修改主機時區和 CloudSQL 時區)
- [x] 調整：文章列表頁(/)，新增 “文章是幾天/分鐘前更新” 的欄位
- [x] 調整：爬蟲狀態頁(/status)，新增 “爬蟲是幾天/分鐘前更新” 的欄位

### week4 進度：新增 Category 功能
- [x] 新增：新增爬蟲爬取網站*7
- [x] 新增：Category 共四大類 ( GoogleBlog, GTM, GA, SEO) 動態網頁
- [x] 新增：Category 的 RSS 網址
- [x] 調整：重構 Flask 架構，修改成使用工廠模式
- [x] 調整：選擇深色模式，切換 Category 頁面後深色模式會跳回淺色模式 (用 cookie 存判斷值來解決)
- [x] 調整：爬蟲爬到資訊會有 html 元素 - 使用正規處理
- [x] 調整：手機版字體會擋到 - 調整手機版型

### week5 進度：Docker 部署
- [x] 完成： Docker compose ( Flask + Nginx ) 部署在 GCP 上
- [x] 完成： CDN Cloudflare 和 SSL Certificate 設定
- [x] 完成： 定時爬蟲 Cron Job 設定
- [x] 完成： Line Bot 串接 RSS 的 category 群組
- [x] 調整： 選擇深色模式後，轉換頁面時，會先閃白色在轉成深色模式
- [x] 調整： 處理爬蟲如果單一噴錯的話，會直接 drop 所有資訊


## 三. 關於

感謝 Huli 的每週固定時間討論專案和指導須改進的地方，以及[前端引路人計劃](https://medium.com/@hulitw/mentorship-program-350db93d5c9c)
