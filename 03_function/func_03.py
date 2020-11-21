#キーワード引数(省略値)
def hamspamfactory(spams=3,hams=5):
    print("Spam! " * spams)
    print("Ham! " * hams)

hamspamfactory()
hamspamfactory(2,2)
hamspamfactory(hams=7)