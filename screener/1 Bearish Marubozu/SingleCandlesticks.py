
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
    

       
       