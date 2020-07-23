A script that will check if a given Rogue item is in stock at a given Rogue url. The script will text you if the item is in stock. The text functionality requires a twilio account.

To run
```
python3 instock.py
```

To run tests
```
python3 instocktest.py
```

Add it to your crontab to run every 3 minutes
```
*/3 * * * * python3 instock.py >> instock_log.txt
```

and rotate the log using log rotate create a file called instock at /etc/logrotate.d/ and
add the following
```
<path to instock_log.txt>
{
daily
size 1M
rotate 1
}
```