



# Memo      

* sql的語法的寫入順序是非常嚴格的，需要依select...from...where…group by…having…order by..limit...的順序輸入
![](.\images\image4.jpg)        

## 分散式系統的大分類：
1. 分散式計算：Spark, Flink, Impala, Presto
2. 分散式儲存：分散式的檔案系統 HDFS, S3, Minio；分散式的資料庫 Redis, Cassandra, Elasticsearch, MongoDB


## 雲端資料倉儲      
雲端資料倉儲規劃，從以下四個層面介紹規劃流程：資料來源、分析需求、資料工作流(Data Pipeline)、資料建模(Data Modeling)
![](.\images\image3.jpg)        
1. 資料來源：用來提供DE做完整的pipeline 規劃。存放位置-地端&雲端；更新頻率-批次&即時；資料格式-結構&非結構。
2. 分析需求：確保資料留存的形式和分析工具可滿足需求， 業務端-管理報表/BI 工具；分析師-以分析目的ETL的衍生資料表/SQL查詢工具；工程師-未經處理的結構與非結構資料/模型開發工具。
3. 資料工作流：掌握資料倉儲最前端的資料源，以及最末端的分析需求後，即可設計End to End工作流。
4. 資料建模：定義衍生資料表的欄位、值域和關聯，以描述現實業務行為。在資料工作流中，大量資料工程會投入在資料湖泊-衍生資料表 (Derived Table)這段，且隨業務發展將持續ETL(Extract、Transform Load)，定期上架新衍生資料表或欄位。

* 為提升資料運用的彈性，現代的資料倉儲通常會多規劃一層資料湖泊(Data Lake)架構，用以儲存末經整理過的原始資料


