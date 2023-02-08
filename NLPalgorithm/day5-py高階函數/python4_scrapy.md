

# python 實作- 爬蟲         


建立虛擬環境            






## 1. 建立虛擬環境     

```linux
pip install virtualenvwrapper

vim ~/.bash_profile
sudo find / -name virtualenvwrapper.sh
source ~/.bash_profile

workon      #列出虛擬環境 
mkvirtualenv spider     #創建虛擬環境

```

## Anaconda-用conda创建python虚拟环境     
https://zhuanlan.zhihu.com/p/94744929

2. conda常用的命令       

    1) 查看安装了哪些包         
    conda list      

    2) 查看当前存在哪些虚拟环境      
    conda env list          
    conda info -e           

    3) 检查更新当前conda         
    conda update conda      

3. Python创建虚拟环境        
conda create -n your_env_name python=x.x        
* anaconda命令创建python版本为x.x，名字为your_env_name的虚拟环境。your_env_name文件可以在Anaconda安装目录envs文件下找到。       

4. 激活或者切换虚拟环境      
打开命令行，输入python --version检查当前 python 版本。          

Linux:  source activate your_env_nam            
Windows: activate your_env_name         

5. 对虚拟环境中安装额外的包     
conda install -n your_env_name [package]        

6. 关闭虚拟环境(即从当前环境退出返回使用PATH环境中的默认python版本)     
deactivate env_name     
或者`activate root`切回root环境     
Linux下：source deactivate          

7. 删除虚拟环境     
conda remove -n your_env_name --all     

8. 删除环境钟的某个包       
conda remove --name $your_env_name  $package_name       

9. 设置国内镜像
http://Anaconda.org的服务器在国外，安装多个packages时，conda下载的速度经常很慢。清华TUNA镜像源有Anaconda仓库的镜像，将其加入conda的配置即可：       
* 添加Anaconda的TUNA镜像        
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/         
* TUNA的help中镜像地址加有引号，需要去掉        
* 设置搜索时显示通道地址        
conda config --set show_channel_urls yes        

10. 恢复默认镜像            
conda config --remove-key channels          



## 創建第一個爬蟲項目       
```linux
activate nlptest        
(nlptest)           
conda config --add channels https://sfai-ui-qas.k8sprd-wzs.k8s.wistron.com.cn/login 
pip install scrapy  
pip install mysqlclient

cd day5-py高階函數      #到workspace
scrapy startproject nlp_spider
cd nlp_spider

scrapy genspider hi https://cn.bing.com/search?q=%EF%BD%88%EF%BD%89&PC=U316&FORM=CHROMN
cd nlp_spider
cd spiders
```

修改 day5-py高階函數/nlp_spider/nlp_spider/main.py
更多工具>開發者工具
```linux
response.css('c-container')
response.css('c-container::attr(title)').extract()
# 
```


