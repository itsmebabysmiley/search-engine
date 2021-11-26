# Magna search engine prototype

<img src="./static/images/MangsS-Logo.png" width="50%" />

## About the project

&nbsp;&nbsp;&nbsp;&nbsp;This is magna search engine prototype. It's part of ITCS414 Information Storage and Retrieval project.  
&nbsp;&nbsp;&nbsp;&nbsp; Magna search focuses on resolving issues

1. Persons who have had difficulty finding magna.
2. People who have a basic understanding of manga, including character names, writers, and genres.

&nbsp;&nbsp;&nbsp;&nbsp; We decided to build a search engine that would tackle these issues by searching using a query. This prototype contians around 100 data sample that we manually collect from [animenewsnetwork](https://www.animenewsnetwork.com/)

## Contributes

1. Pranungfun Prapaenee (MUICT#17)
2. Nopparat Pengsuk (MUICT#17)
3. Pongsakorn Piboonpongpun (MUICT#17)

## Requirements

1. ```Elasticsearch```
2. ```Flask```
3. ```ndjson```

## Installation Guide

This prototype runs on [ElasticSearch](https://www.elastic.co/)

**Memory Configuration (Windows)**

When you run ```ElasticSearch``` Server for first time, it will take half of you memory by defult. To set the limit of memory you can create a file ```mem_limit.options``` and put into folder in ElasticSearch```/config/jvm.options.d``` In ```mem_limit.options``` you can specific the memory by  

```bash
-Xms1g
-Xmx1g
```

where 1 is the maximum of your memory to assign to ElasticSearch.

After you run the ElasticSearch server, you can create index name by

```bash
PUT /<index>
```

Then you can load the data set by follow

## How to use elasticsearch_loader.py?

```bash
python elasticsearch_loader.py --file <anyfile.json> --index <index name> --type <anyname>
```

----

## Addtional files

### How to use normalize_data.py?

```bash
python normalize_data.py -i <input_file.json> -o <output_file.json>
```

### THIS WORK IS UNDER MAHIDOL LINCESE
