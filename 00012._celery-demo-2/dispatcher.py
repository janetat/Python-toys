from tasks import math, download

if __name__ == '__main__':
    url = 'https://c-ssl.duitang.com/uploads/item/201111/26/20111126231016_cJFur.jpg'
    download.download_img.apply_async(args=(url, ))
    math.add.apply_async(args=(3,4), queue='add')