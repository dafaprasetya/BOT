from bardapi import BardCookies
from plyer import notification


def aigoblog(soal):
    with open('cookie.txt', 'r') as cb:
        Secure_1PSID = cb.readlines()[0][21:]
    with open('cookie.txt', 'r') as cb:
        Secure_1PSIDTS = cb.readlines()[1][21:]
        
            
    cookie_dict = {
        "__Secure-1PSID": f"{Secure_1PSID.strip()}",
        "__Secure-1PSIDTS": f"{str(Secure_1PSIDTS)}",
    }

    try : 
        bard = BardCookies(cookie_dict=cookie_dict)
        jawab = bard.get_answer(f'{soal}')['content'][:255]
        print(bard.get_answer(f'{soal}')['content'])
        notification.notify(
            title = 'jawaban',
            message = jawab,
            app_icon = None,
            timeout = 10,
        )
        return jawab
    except :
        notification.notify(
            title = 'Error',
            message = 'Terjadi kesalahan silahkan cek cookies',
            app_icon = None,
            timeout = 10,
        )