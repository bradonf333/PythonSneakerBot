# Base URL = http://www.adidas.com/us/nmd_r1-shoes/BZ0220.html?forceSelSize=BZ0220_640

def URLGen(model, size):
    BaseSize = 580
    #Base Size for the Shoe is 6.5
    #Minus 6.5 from the shoe size to give a base, 6.5 would equal 0
    ShoeSize = size - 6.5
    #Number that we need to add to base size to equal the desired shoe size
    ShoeSize = ShoeSize * 20
    #Gives us the desired shoe size code
    RawSize = ShoeSize + BaseSize
    #Convert RawSize to int
    ShoeSizeCode = int(RawSize)
    #Build the URL
    URL = 'http://www.adidas.com/us/nmd_r1-shoes/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
    return URL

print(URLGen('BZ0220',9.5))