def preparoDeMacarrao(*serveonumerode, serve="2 pessoas"):
    print("preparando um macarrao", serve, "para isso coloque:")
    for serve in serveonumerode:
         print("-", serve)


preparoDeMacarrao("2 pacotes de macarrao" , "2 molhos de tomate", serve="5 pessoas")
preparoDeMacarrao("3 pacotes de macarrao" , "3 molhos de tomate", serve="para tres pessoas")
preparoDeMacarrao("1 pacote de macarrao" , "1 molho de tomate", serve="para uma pessoa")
preparoDeMacarrao()