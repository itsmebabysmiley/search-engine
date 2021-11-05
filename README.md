# Search engine prototype

## Contributes

1. Pranungfun Prapaenee 6288034
2. Nopparat Pengsuk 6288103
3. Pongsakorn Piboonpongpun 6288107

## About the project

Search engine prototype is using Elasticsearch and flask. We develop search engine for magna(Japan)<br/>
This prototype contians around 100 data sample that we manually collect from [animenewsnetwork](https://www.animenewsnetwork.com/)

## Requirement

1. please use index as ```magna_index```

## How to use elasticsearch_loader.py?

```bash
python elasticsearch_loader.py --file <file.json> --index <index_name> --type <type>
```


## How to use normalize_data.py?

```bash
python normalize_data.py -i <input_file.json> -o <output_file.json>
```

### THIS WORK IS UNDER MAHIDOL LINCESE
