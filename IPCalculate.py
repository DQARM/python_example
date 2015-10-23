
while (1):
    print ""
    RawIP=raw_input("Please Input the IP address(x.x.x.x/x) or 'exit'>")
    print 'Your input is '+RawIP

    if RawIP=='exit':
        break
    if (RawIP.find('/') == -1):
        print "No '/' in input string"
	continue
    if (RawIP.find('.') == -1):
        print "No '.' in input string"
        continue
    if (RawIP.count('.',0,len(RawIP))!=3 or RawIP.count('/',0,len(RawIP))!=1 ):
        print "Input String is not correct format"
        continue

    StopFlag=0

    IP=RawIP.split('/')[0]                 #x.x.x.x
    Mask= RawIP.split('/')[1]              
    if Mask=='':
        print "Illegal Mask"
        StopFlag=1
		
    for ch in Mask:
        if (ch.isalpha()):
            print "Your Mask is Alphabet"
            StopFlag=1
            break      # break for for_loop

    if (StopFlag==1):
        continue
    elif (int(Mask)>32 or int(Mask)<1):
        print "Your mask is Greater than 32 or Less than 1"
        continue

    for item in IP.split('.'):
        
        if (StopFlag==1):
            break   # break for for_loop
        elif(item==''):
            print "Illegal IP"
            StopFlag=1			
            break
        else:
            for ch in item:
                if (ch.isalpha()):
                    print "Alpahbet in your input string(IP Part)"
                    StopFlag=1
                    break      # break for "for ch in item" 
            if (StopFlag==1):
                continue
            elif ((int(item)>255) or (int(item)<0)):
                print "Your number is greater than 255 or less than 0"
                StopFlag=1
                break      # break for for_loop

    if (StopFlag==1):
        continue    #Restart While(1)

    Bin_IP =0
    Bin_Broadcast_Mask =1
    Bin_Netid_Mask=1
    Bin_Broadcast_Mask=1
    for subip in IP.split("."):
        #print 'subip='+subip
        #print '{0:b}'.format(int(subip))
        Bin_IP=(Bin_IP<<8)+int(subip)
        #print '{0:b}'.format(Bin_IP)
        #print '%b',Bin_IP
        #Bin_IP.format(10)

    for i in range(int(Mask)-1):
        Bin_Netid_Mask=(Bin_Netid_Mask<<1) + 1
        #print "Bin_Mask"+str(Bin_Mask)
    Bin_Netid_Mask=Bin_Netid_Mask<< (32-int(Mask))
    for i in range(32-int(Mask)-1):
        Bin_Broadcast_Mask=(Bin_Broadcast_Mask<<1)+1
    print "Bin_Broadcast_Mask"+'{0:b}'.format(int(Bin_Broadcast_Mask))
    Bin_NetID= Bin_IP & Bin_Netid_Mask
    Bin_Broadcast_IP=Bin_IP | (Bin_Broadcast_Mask)
    NetID= str(Bin_NetID>>24)+"."+str((Bin_NetID&0X00FF0000)>>16)+"."+str((Bin_NetID&0X0000FF00)>>8)+"."+str(Bin_NetID&0X000000FF)
    Broadcast_IP= str(Bin_Broadcast_IP>>24)+"."+str((Bin_Broadcast_IP&0X00FF0000)>>16)+"."+str((Bin_Broadcast_IP&0X0000FF00)>>8)+"."+str(Bin_Broadcast_IP&0X000000FF)
    #print "here"+str(Bin_Broadcast_IP<<8)
    print "Host IP(Dec): "+IP
    print "Mask(Dec): "+Mask
    print "Host IP(Bin): "+ '{0:b}'.format(Bin_IP) 
    print "Mask(Bin):   "+ '{0:b}'.format(int(Bin_Netid_Mask))
    print "Broadcast IP(Bin): " + '{0:b}'.format(int(Bin_Broadcast_IP))
    print "Broadcast IP(Dec): " + Broadcast_IP
    print "Network ID IP (Bin): " +'{0:b}'.format(int(Bin_NetID))
    print "Network ID IP (Dec): "+NetID
    #print RawIP.split("/")
    #print RawIP.isalpha()

