# 110Project_delete_back-pdf2img

需要用pip安裝的package:\
1.numpy \
2.cv2\
3.pdf2image\
4.PIL

關於pdf_to_jpg.py的pdf2img的package:\
請先去安裝poppler:
https://github.com/oschwartz10612/poppler-windows/releases/ \
修改你下載poppler檔案的路徑到poppler_path即可使用

關於pdf_to_jpg.py和delete_back.py:\
老師給的圖檔分成了兩種名字\
一種是EKG_編號_post，另一種是EKG_編號_pre
因此需要改兩次路徑抓取檔案(code上有註明)

請把所有檔案(number.csv\delete_back.py\pdf_to_jpg.py)放在同個資料夾，不然會抓不到編號

看到兩種錯誤:\
1.I/O ERROR\
2.error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor')

請勿擔心，是找不到這個編號然後print出來只是偵錯使用\
(因為老師給的圖檔不是所有編號都有的zzz)
