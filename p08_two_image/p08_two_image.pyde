# p08_two_image
size(1000,667) # 用你的background.jpg圖的大小
imgBG = loadImage('background.jpg')
image(imgBG, 0, 0)
imgKitty = loadImage('kitty.png') # 找半透明的png圖
for i in range(10):
    image(imgKitty, 100*i, 0, 200,230)
