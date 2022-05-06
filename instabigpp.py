import instaloader
ig = instaloader.Instaloader()
profile = input("Kullanici adi giriniz : ")
ig.download_profile(profile, profile_pic_only = True)