twitdump
========

A twitter profile exporter that doesn't require twitter api, written in python.

Works in all platforms, requires BeautifulSoup library installed.


## Usage
```
python twitdump.py twitter_profile > tweets.txt
```

## Information
Gets all tweets of given public twitter profile in reverse chronological order. Doesn't require twitter api. Either you can display the output in the command-line interface by default, or save the output to a file with ` > tweets.txt` command, filename is obviously optional.
[Here](https://github.com/carroty/twitdump/blob/master/tweets.txt) is an example of output file.

## License
The MIT License. (see [LICENSE file](https://github.com/carroty/twitdump/blob/master/LICENSE))
