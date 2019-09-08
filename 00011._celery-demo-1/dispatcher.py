from tasks import download_img, add

if __name__ == '__main__':
    url = ''
    download_img.apply_async(args=(url, ))
    add.apply_async(args=(3,4), queue='add')