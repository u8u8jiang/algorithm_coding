專案七 伺服器日誌資料清洗分析      
專案八 氣象資料分析         


## Data:         
1. win_application.txt: 應用程序日誌記錄服務器上安裝的一些應用程序或系統默認程序的事件。
例如實例上運行的站點服務，MySQL，PHP，IIS等相關的應用程序的事件記錄。           
2. win_security.txt: 安全日誌記錄服務器的登錄信息，或一些策略的審核事件。
遠程登錄時，如果是正常的登錄，會顯示審核成功。如果是異常的，比如密碼錯誤等，就會提示審核失敗。 
3. win_system.txt: 系統日志記錄系統異常引起的事件。可以查看系統更新，內存資源不足等系統日誌。
感嘆號（！） 表示警告，一般不會嚴重影響使用。內存資源不足等多次警告事件可能會導致主機卡慢或假死的現象     
    * computer manager>system tools>event viewer>windowslogs: application, security, system        
4. win_operational.txt: 記錄了用戶遠程桌面的訪問日誌，可以通過該日誌定位遠程登錄的相關問題。            
    * computer manager>system tools>event viewer>applications and services logs>microsoft>windowsTerminalServices-LocalSessionManager>Operational       

如何使用Windows事件查看器查看实例运行日志       
https://help.aliyun.com/document_detail/41044.html


Next:   
1. 試著發現甚麼...並轉成格式化數據      
2. 視覺化呈現數據: time series, pie, 雷達圖?, 訪問頻次...                            
3. 可能可以作甚麼題目嗎? 訪問頻率 (访问次数、停留时间、抓取量、目录抓取统计)            


- 查看訪問最多的xx (頁面, ip)                       
- 某個 xx (頁面, ip)被訪問次數, 由大到小...     
- 某個ip訪問了那些頁面...       
日誌: 信息, 調適, 警告, 錯誤, 警報...       
Windows日志至少包括应用程序、安全和系统。最重要的是安全日志，登录、注销、资源访问记录的地方。       

【干货】日志管理与分析（一）——日志收集及来源        
https://blog.csdn.net/systemino/article/details/98515158




















運用技術點
1. 資料科學原理與資料處理
    * 資料科學原理 
    * 資料處理流程 
    * 資料分析好助手Jupyter notebook 
    * 資料科學模組Numpy 
    * 統計分析模組Pandas
    * 資料質量分析 
    * 資料特徵分析      

2. 特徵工程
    * 通過真實資料觀察大局 
    * 選擇效能指標、檢查假設 獲取資料（建立工作區，快速檢視資料結構，建立測試集）
    * 從資料視覺化中探索資料的奧祕（將資料視覺化、尋找相關性、試驗不同的屬性組合） 
    * 機器學習訓練前的準備（資料清理、自定義轉換器、特徵縮放、轉換流水線） 
    * 選擇和訓練模型（評估訓練集、交叉驗證、分析最佳模型及其錯誤、測試集評估）  
    * 模型的調優 
    * 分析最佳模型和測試集評估 
    * 系統維護和監控        
 
練習目標：資料分析和資料探勘、機器學習/Jupyter notebook的安裝、使用、魔法命令/Numpy矩陣和隨機數生成、ndarray基本操作、ndarray的合併與分割、矩陣運算、聚合操作、arg運算、比較運算/Pandas的資料結構、資料中的選取與操作、載入各種資料、排序與合併、資料彙總、資料分組與透視表、時間序列/資料的視覺化/資料獲取和載入、資料清洗/資料內容處理與分析/特徵工程原理         

就業方向：【Python資料分析師】          
