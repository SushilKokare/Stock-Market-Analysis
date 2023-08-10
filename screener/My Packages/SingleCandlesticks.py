
class BullishMarubozu:
    def getbullishmarobozu(df):

        if('OPEN' in df.columns):

            bls={}  # Bullish Maruozu For Sorting

            for ind in df.index:
                # bullish marubozu
                if(df['OPEN'][ind] < df['CLOSE'][ind] ): 
                    buffer = ( (df['CLOSE'][ind]- df['OPEN'][ind]) /100)*10
                    if(( df['HIGH'][ind] - df['CLOSE'][ind] ) < buffer ):
                        if(( df['OPEN'][ind] - df['LOW'][ind] ) < buffer ):
                            if( ( df['CLOSE'][ind] - df['OPEN'][ind] ) >  ((df['CLOSE'][ind] / 100)*1 ) ): 
                                #print(df['SYMBOL'][ind], df['CLOSE'][ind])
                                bls[df['SYMBOL'][ind] ] = ((buffer/df['CLOSE'][ind])*100)

            print("---------------Bullish Marubozu----------------")
            print("                      ")
            print(bls)
            print("           --           ")
            print("Sorted In Descending Order Of Change In %")
            print("                      ")
            print(sorted(bls.items(), key =lambda kv:(kv[1], kv[0]),reverse=True))   
            print("")



        elif('Open' in df.columns):
            bls={}  # Bullish Maruozu For Sorting

            print("---------------Bullish Marubozu----------------")
            for ind in df.index:

                # bullish marubozu

                if(df['Open'][ind] < df['Close'][ind] ): 
                    buffer = ( (df['Close'][ind]- df['Open'][ind]) /100)*10
                    if(( df['High'][ind] - df['Close'][ind] ) < buffer ):
                        if(( df['Open'][ind] - df['Low'][ind] ) < buffer ):
                            if( ( df['Close'][ind] - df['Open'][ind] ) >  ((df['Close'][ind] / 100)*1 ) ): 
                                print(ind, df['Close'][ind])
                                #bls[ind] = ((buffer/df['Close'][ind])*100)

# --------------------------------------------------------------------------------------------------------


class BearishMarubozu:
    def getbearishmarobozu(df):

        if('OPEN' in df.columns):

            brs={}  # Bearish Marubozu For Sorting

            for ind in df.index:
                # bearish marubozu
                if(df['CLOSE'][ind] < df['OPEN'][ind] ): 
                    buffer = ( (df['OPEN'][ind]-df['CLOSE'][ind]) /100)*10
                    if(( df['HIGH'][ind] - df['OPEN'][ind] ) < buffer ):
                        if(( df['CLOSE'][ind] - df['LOW'][ind] ) < buffer ):
                            if( ( df['OPEN'][ind] - df['CLOSE'][ind] ) >  ((df['CLOSE'][ind] / 100)*1 ) ): 
                                #print(df['SYMBOL'][ind], df['CLOSE'][ind])
                                brs[df['SYMBOL'][ind]]=((buffer/df['CLOSE'][ind])*100)


            print("---------------Bearish Marubozu----------------")
            print("                      ")
            print(brs)
            print("           --           ")
            print("Sorted In Descending Order Of Change In %")
            print("                      ")
            print(sorted(brs.items(), key =lambda kv:(kv[1], kv[0]),reverse=True))   
            print("")


        elif('Open' in df.columns):
            brs={}  # Bearish Marubozu For Sorting


            print("---------------Bearish Marubozu----------------")
            for ind in df.index:


                # bearish marubozu
                if(df['Close'][ind] < df['Open'][ind] ): 
                    buffer = ( (df['Open'][ind]-df['Close'][ind]) /100)*10
                    if(( df['High'][ind] - df['Open'][ind] ) < buffer ):
                        if(( df['Close'][ind] - df['Low'][ind] ) < buffer ):
                            if( ( df['Open'][ind] - df['Close'][ind] ) >  ((df['Close'][ind] / 100)*1 ) ): 
                                print(ind, df['Close'][ind])
                                #brs[ind]=((buffer/df['Close'][ind])*100)
    

# --------------------------------------------------------------------------------------------------------

class SpinningTop:
    def getspinningtop(df):
        bst={} # Blue Spinning Top
        rst={} # Red Spinning Top

        if('OPEN' in df.columns):

            for ind in df.index:
                if(df['OPEN'][ind] < df['CLOSE'][ind] ):
                    bper=round(((float(df['CLOSE'][ind])-float(df['OPEN'][ind]))/float(df['CLOSE'][ind]))*100,4) # body percentage
                    us=round(((float(df['HIGH'][ind])-float(df['CLOSE'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['OPEN'][ind])-float(df['LOW'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Lower Shadow
                    if(bper>0.32 and bper<1.8 and us>0.8 and ls>0.8 and abs(us-ls)<0.5):
                        #print(df['SYMBOL'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        bst[df['SYMBOL'][ind]]= bper

                elif(df['CLOSE'][ind] < df['OPEN'][ind] ):
                    bper=round(((float(df['OPEN'][ind])-float(df['CLOSE'][ind]))/float(df['CLOSE'][ind]))*100,4) # body percentage
                    us=round(((float(df['HIGH'][ind])-float(df['OPEN'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['CLOSE'][ind])-float(df['LOW'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Lower Shadow
                    if(bper>0.32 and bper<1.8 and us>0.8 and ls>0.8 and abs(us-ls)<0.5):
                        #print(df['SYMBOL'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        rst[df['SYMBOL'][ind]]= bper


                elif(df['CLOSE'][ind] == df['OPEN'][ind] ):
                    bper=0
                    #per=round(((float(df['OPEN'][ind])-float(df['CLOSE'][ind]))/float(df['CLOSE'][ind]))*100,4)
                    #print(df['SYMBOL'][ind] +"="+str(per))
                    #print("-------------------------------------------")
                    pass



        elif('Open' in df.columns):

            for ind in df.index:
                if(df['Open'][ind] < df['Close'][ind] ):
                    bper=round(((float(df['Close'][ind])-float(df['Open'][ind]))/float(df['Close'][ind]))*100,4) # body percentage
                    us=round(((float(df['High'][ind])-float(df['Close'][ind]))/float(df['Close'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['Open'][ind])-float(df['Low'][ind]))/float(df['Close'][ind]))*100,4)  # Lower Shadow
                    if(bper>0.32 and bper<1.8 and us>0.8 and ls>0.8 and abs(us-ls)<0.8):
                        #print(df['Symbol'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        #bst[df['Symbol'][ind]]= bper
                        bst[ind]=df['Close'][ind]

                elif(df['Close'][ind] < df['Open'][ind] ):
                    bper=round(((float(df['Open'][ind])-float(df['Close'][ind]))/float(df['Close'][ind]))*100,4) # body percentage
                    us=round(((float(df['High'][ind])-float(df['Open'][ind]))/float(df['Close'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['Close'][ind])-float(df['Low'][ind]))/float(df['Close'][ind]))*100,4)  # Lower Shadow
                    if(bper>0.32 and bper<1.8 and us>0.8 and ls>0.8 and abs(us-ls)<0.8):
                        #print(df['Symbol'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        #rst[df['Symbol'][ind]]= bper
                        rst[ind]=df['Close'][ind]

                elif(df['Close'][ind] == df['Open'][ind] ):
                    bper=0
                    #per=round(((float(df['Open'][ind])-float(df['Close'][ind]))/float(df['Close'][ind]))*100,4)
                    #print(df['Symbol'][ind] +"="+str(per))
                    #print("-------------------------------------------")
                    pass
            
        print("BLUE SPINNING TOP")
        print(bst)
        print("-------------------------------------------")
        print("RED SPINNING TOP")
        print(rst)



# --------------------------------------------------------------------------------------------------------


class Doji:
    def getdoji(df):

        bd={} # Blue Doji
        rd={} # Red Doji

        if('OPEN' in df.columns):

            for ind in df.index:
                if(df['OPEN'][ind] < df['CLOSE'][ind] ):
                    bper=round(((float(df['CLOSE'][ind])-float(df['OPEN'][ind]))/float(df['CLOSE'][ind]))*100,4) # body percentage
                    us=round(((float(df['HIGH'][ind])-float(df['CLOSE'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['OPEN'][ind])-float(df['LOW'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Lower Shadow
                    if(bper>=0 and bper<=0.32 and us>0.1 and ls>0.1):
                        #print(df['SYMBOL'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        bd[df['SYMBOL'][ind]]= bper

                elif(df['CLOSE'][ind] < df['OPEN'][ind] ):
                    bper=round(((float(df['OPEN'][ind])-float(df['CLOSE'][ind]))/float(df['CLOSE'][ind]))*100,4) # body percentage
                    us=round(((float(df['HIGH'][ind])-float(df['OPEN'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['CLOSE'][ind])-float(df['LOW'][ind]))/float(df['CLOSE'][ind]))*100,4)  # Lower Shadow
                    if(bper>=0 and bper<=0.32 and us>0.1 and ls>0.1):
                        #print(df['SYMBOL'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        rd[df['SYMBOL'][ind]]= bper


                elif(df['CLOSE'][ind] == df['OPEN'][ind] ):
                    bper=0
                    #per=round(((float(df['OPEN'][ind])-float(df['CLOSE'][ind]))/float(df['CLOSE'][ind]))*100,4)
                    #print(df['SYMBOL'][ind] +"="+str(per))
                    #print("-------------------------------------------")
                    pass



        elif('Open' in df.columns):

            for ind in df.index:
                if(df['Open'][ind] < df['Close'][ind] ):
                    bper=round(((float(df['Close'][ind])-float(df['Open'][ind]))/float(df['Close'][ind]))*100,4) # body percentage
                    us=round(((float(df['High'][ind])-float(df['Close'][ind]))/float(df['Close'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['Open'][ind])-float(df['Low'][ind]))/float(df['Close'][ind]))*100,4)  # Lower Shadow
                    if(bper>=0 and bper<=0.32 and us>0.1 and ls>0.1):
                        #print(df['Symbol'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        #bd[df['Symbol'][ind]]= bper
                        bd[ind]=df['Close'][ind]

                elif(df['Close'][ind] < df['Open'][ind] ):
                    bper=round(((float(df['Open'][ind])-float(df['Close'][ind]))/float(df['Close'][ind]))*100,4) # body percentage
                    us=round(((float(df['High'][ind])-float(df['Open'][ind]))/float(df['Close'][ind]))*100,4)  # Upper Shadow
                    ls=round(((float(df['Close'][ind])-float(df['Low'][ind]))/float(df['Close'][ind]))*100,4)  # Lower Shadow
                    if(bper>=0 and bper<=0.32 and us>0.1 and ls>0.1):
                        #print(df['Symbol'][ind] +"="+str(per) +" Per = "+str(per)+" US = "+str(us)+" LS = "+str(ls))
                        #rd[df['Symbol'][ind]]= bper
                        rd[ind]=df['Close'][ind]

                elif(df['Close'][ind] == df['Open'][ind] ):
                    bper=0
                    #per=round(((float(df['Open'][ind])-float(df['Close'][ind]))/float(df['Close'][ind]))*100,4)
                    #print(df['Symbol'][ind] +"="+str(per))
                    #print("-------------------------------------------")
                    pass

        print("BLUE DOJI")
        print(bd)
        print("-------------------------------------------")
        print("RED DOJI")
        print(rd)



# --------------------------------------------------------------------------------------------------------


