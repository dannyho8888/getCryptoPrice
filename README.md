## getCryptoPrice
This script is built to get the specific cryptocurrency pricees in your terminal

## Getting start
Go coinMarketCap to get your free api key first. Then paste the key to the key.py file. Run the .sh file and type the cryptocurrency you want. The price will show up properly.
```sh
 ~/yourOwnPath/getCryptoPrice/getSymbol.sh btc eth
``` 
![alt text](https://na.cx/i/JUcDw2t.png)

then go your .zshrc and alias the above command with "price"

```sh
 nano ~/.zshrc 
```
or whatever shell rc file you're using.

Then paste the below command inside the .zshrc file
```sh
 alias price="~/yourOwnPath/getCryptoPrice/getSymbol.sh"
```
Finally use source command to activate the .zshrc file
```sh
 source ./zshrc
```

Reopen the terminal and you're ready to go
![alt text](https://na.cx/i/FarHYHt.png)
 

