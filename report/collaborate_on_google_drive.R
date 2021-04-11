rmdrive::upload_rmd(
  file       = "report/make_table_figure",   # specifies the local `.Rmd` file (without extension)
  path       = "https://drive.google.com/drive/folders/1m83RZo-Y0Bf8wujApX7ctI3N-NBrYvgK"        # specifies a folder in Google Drive (optional; if not specified, the home directory of My Drive or the Team Drive is used)
)

rmdrive::render_rmd(
  file = "report/make_table_figure",
  path       = "https://drive.google.com/drive/folders/1m83RZo-Y0Bf8wujApX7ctI3N-NBrYvgK" 
)
