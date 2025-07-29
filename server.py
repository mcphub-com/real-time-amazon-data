import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-amazon-data'

mcp = FastMCP('real-time-amazon-data')

@mcp.tool()
def product_search(query: Annotated[str, Field(description='Search query (supports both free-form text queries or a product asin).')],
                   page: Annotated[Union[int, float, None], Field(description='Results page to return. Default: 1 Default: 1')] = None,
                   country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                   sort_by: Annotated[Literal['RELEVANCE', 'LOWEST_PRICE', 'HIGHEST_PRICE', 'REVIEWS', 'NEWEST', 'BEST_SELLERS', None], Field(description='Return the results in a specific sort order. Default: RELEVANCE Allowed values: RELEVANCE, LOWEST_PRICE, HIGHEST_PRICE, REVIEWS, NEWEST, BEST_SELLERS')] = None,
                   category_id: Annotated[Union[str, None], Field(description='Find products in a specific category / department (e.g. computers-intl-ship). Use the Product Category List endpoint to get a list of valid categories and their ids for the country specified in the request. For numeric Amazon category IDs, use the category parameter instead. Default: aps (All Departments)')] = None,
                   category: Annotated[Union[str, None], Field(description='Filter by specific numeric Amazon category. The category ID can be obtained from the Amazon category results URL, for example: https://amazon.com/s?node=2858778013 - the Amazon Category ID is 2858778013. Multiple category values can be separated by comma (e.g. categoryId1,categoryId2).')] = None,
                   min_price: Annotated[Union[int, float, None], Field(description='Only return product offers with price greater than a certain value. Specified in the currency of the selected country. For example, in case country=US, a value of 105.34 means $105.34. Default: 0')] = None,
                   max_price: Annotated[Union[int, float, None], Field(description='Only return product offers with price lower than a certain value. Specified in the currency of the selected country. For example, in case country=US, a value of 105.34 means $105.34. Default: 0')] = None,
                   product_condition: Annotated[Literal['ALL', 'NEW', 'USED', 'RENEWED', 'COLLECTIBLE', None], Field(description='Return products in a specific condition. Default: ALL Allowed values: ALL, NEW, USED, RENEWED, COLLECTIBLE')] = None,
                   brand: Annotated[Union[str, None], Field(description="Find products with a specific brand. Multiple brands can be specified as a comma (,) separated list. The brand values can be seen from Amazon's search left filters panel, as seen here. Examples: SAMSUNG Google,Apple")] = None,
                   seller_id: Annotated[Union[str, None], Field(description='Find products sold by specific seller (merchant). Multiple sellers can be specified as a comma (,) separated list. Examples: A02211013Q5HP3OMSZC7W AM7YCCDZROLB2,A1D09S7Q0OD6TH')] = None,
                   is_prime: Annotated[Union[bool, None], Field(description='Only return prime products. Default: false')] = None,
                   deals_and_discounts: Annotated[Literal['NONE', 'ALL_DISCOUNTS', 'TODAYS_DEALS', None], Field(description='Return deals and discounts in a specific condition. Default: NONE Allowed values: NONE, ALL_DISCOUNTS, TODAYS_DEALS')] = None,
                   four_stars_and_up: Annotated[Union[bool, None], Field(description='Return product listings with ratings of 4 stars & up.')] = None,
                   language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                   additional_filters: Annotated[Union[str, None], Field(description="Any filters available on the Amazon page but not part of this endpoint's parameters. The filter values can be extracted from the rh parameter in the Amazon search URL after applying the filter of interest on the Amazon search results page. Multiple filters are supported and can be separated by comma (,). For example, when searching for science books with the Paperback book format filter selected, the Amazon URL is: https://www.amazon.com/s?k=science+books&rh=p_n_feature_browse-bin%3A2656022011 and the rh parameter value is p_n_feature_browse-bin%3A2656022011 - To filter for Paperback books, set the value of additional_parameters=p_n_feature_browse-bin%3A2656022011.")] = None,
                   fields: Annotated[Union[str, None], Field(description='A comma separated list of product fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_url,is_best_seller,sales_volume')] = None) -> dict: 
    '''Search for products & offers on Amazon with pagination support and multiple filters and options such as sort option, price range, product condition filter, and more.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'page': page,
        'country': country,
        'sort_by': sort_by,
        'category_id': category_id,
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
        'product_condition': product_condition,
        'brand': brand,
        'seller_id': seller_id,
        'is_prime': is_prime,
        'deals_and_discounts': deals_and_discounts,
        'four_stars_and_up': four_stars_and_up,
        'language': language,
        'additional_filters': additional_filters,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def products_by_category(category_id: Annotated[str, Field(description='The Amazon category for which to return results. The category ID can be obtained from the Amazon category results URL, for example: https://amazon.com/s?node=2858778013 - the Amazon Category ID is 2858778013. Multiple category values can be separated by comma (e.g. categoryId1,categoryId2).')],
                         page: Annotated[Union[int, float, None], Field(description='Page to return. Default: 1 Default: 1')] = None,
                         country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                         sort_by: Annotated[Literal['RELEVANCE', 'LOWEST_PRICE', 'HIGHEST_PRICE', 'REVIEWS', 'NEWEST', 'BEST_SELLERS', None], Field(description='Return the results in a specific sort order. Default: RELEVANCE Allowed values: RELEVANCE, LOWEST_PRICE, HIGHEST_PRICE, REVIEWS, NEWEST, BEST_SELLERS')] = None,
                         min_price: Annotated[Union[int, float, None], Field(description='Only return product offers with price greater than a certain value. Specified in the currency of the selected country. For example, in case country=US, a value of 105.34 means $105.34.')] = None,
                         max_price: Annotated[Union[int, float, None], Field(description='Only return product offers with price lower than a certain value. Specified in the currency of the selected country. For example, in case country=US, a value of 105.34 means $105.34.')] = None,
                         product_condition: Annotated[Literal['ALL', 'NEW', 'USED', 'RENEWED', 'COLLECTIBLE', None], Field(description='Return products in a specific condition. Default: ALL Allowed values: ALL, NEW, USED, RENEWED, COLLECTIBLE')] = None,
                         brand: Annotated[Union[str, None], Field(description="Only return products of a specific brand. Multiple brands can be specified as a comma (,) separated list. The brand values can be seen from Amazon's search left filters panel, as seen here. Examples: SAMSUNG Google,Apple")] = None,
                         is_prime: Annotated[Union[bool, None], Field(description='Only return prime products. Default: false')] = None,
                         deals_and_discounts: Annotated[Literal['NONE', 'ALL_DISCOUNTS', 'TODAYS_DEALS', None], Field(description='Return deals and discounts in a specific condition. Default: NONE Allowed values: NONE, ALL_DISCOUNTS, TODAYS_DEALS')] = None,
                         four_stars_and_up: Annotated[Union[bool, None], Field(description='Return product listings with ratings of 4 stars & up.')] = None,
                         language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                         additional_filters: Annotated[Union[str, None], Field(description="Any filters available on the Amazon page but not part of this endpoint's parameters. The filter values can be extracted from the rh parameter in the Amazon search URL after applying the filter of interest on the Amazon search results page. Multiple filters are supported and can be separated by comma (,). For example, when searching for science books with the Paperback book format filter selected, the Amazon URL is: https://www.amazon.com/s?k=science+books&rh=p_n_feature_browse-bin%3A2656022011 and the rh parameter value is p_n_feature_browse-bin%3A2656022011 - To filter for Paperback books, set the value of additional_parameters=p_n_feature_browse-bin%3A2656022011.")] = None,
                         fields: Annotated[Union[str, None], Field(description='A comma separated list of product fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_url,is_best_seller,sales_volume')] = None) -> dict: 
    '''Get products & offers in a specific Amazon category with pagination support and multiple filters and options such as sort option, price range, product condition filter, and more.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/products-by-category'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category_id': category_id,
        'page': page,
        'country': country,
        'sort_by': sort_by,
        'min_price': min_price,
        'max_price': max_price,
        'product_condition': product_condition,
        'brand': brand,
        'is_prime': is_prime,
        'deals_and_discounts': deals_and_discounts,
        'four_stars_and_up': four_stars_and_up,
        'language': language,
        'additional_filters': additional_filters,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_details(asin: Annotated[str, Field(description='Product ASIN for which to get details. Supports batching of up to 10 ASINs in a single request, separated by comma. Examples: B08BHXG144 B08PPDJWC8,B07ZPKBL9V,B08BHXG144 Note that each ASIN in a batch request is counted as a single request against the plan quota.')],
                    country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                    more_info_query: Annotated[Union[str, None], Field(description='A query to search and get more info about the product as part of Product Information, Customer Q&As, and Customer Reviews.')] = None,
                    language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                    fields: Annotated[Union[str, None], Field(description='A comma separated list of product fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_url,is_best_seller,sales_volume')] = None) -> dict: 
    '''Get extensive Amazon product details and information available on the Amazon product page by asin, including title, price data, ratings data, photos, product details (brand, weight, package size, model, etc) product variations (colors, sizes, flavors, etc), and many other data points. Here's an example product page: [https://www.amazon.com/dp/B0CMZFCQ6D](https://www.amazon.com/dp/B0CMZFCQ6D).'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/product-details'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'asin': asin,
        'country': country,
        'more_info_query': more_info_query,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_reviews(asin: Annotated[str, Field(description='Product asin for which to get reviews.')],
                    country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                    page: Annotated[Union[int, float, None], Field(description='Results page to return. Default: 1 Default: 1')] = None,
                    sort_by: Annotated[Literal['TOP_REVIEWS', 'MOST_RECENT', None], Field(description='Return reviews in a specific sort order. Default: TOP_REVIEWS Allowed values: TOP_REVIEWS, MOST_RECENT')] = None,
                    star_rating: Annotated[Literal['ALL', '5_STARS', '4_STARS', '3_STARS', '2_STARS', '1_STARS', 'POSITIVE', 'CRITICAL', None], Field(description='Only return reviews with a specific star rating. Default: ALL Allowed values: ALL, 5_STARS, 4_STARS, 3_STARS, 2_STARS, 1_STARS, POSITIVE, CRITICAL')] = None,
                    verified_purchases_only: Annotated[Union[bool, None], Field(description='Only return reviews by reviewers who made a verified purchase.')] = None,
                    images_or_videos_only: Annotated[Union[bool, None], Field(description='Only return reviews containing images and / or videos.')] = None,
                    current_format_only: Annotated[Union[bool, None], Field(description='Only return reviews of the current format (product variant - e.g. Color). By default reviews are returned for all product variants.')] = None,
                    query: Annotated[Union[str, None], Field(description='Find reviews matching a search query.')] = None,
                    language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                    fields: Annotated[Union[str, None], Field(description='A comma separated list of review fields to include in the response (field projection). By default all fields are returned. Example: review_title,review_images,review_date,country')] = None) -> dict: 
    '''Get and paginate through product reviews on Amazon using a logged in user cookie string. Each page contains up to 10 reviews.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/product-reviews'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'asin': asin,
        'country': country,
        'page': page,
        'sort_by': sort_by,
        'star_rating': star_rating,
        'verified_purchases_only': verified_purchases_only,
        'images_or_videos_only': images_or_videos_only,
        'current_format_only': current_format_only,
        'query': query,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_offers(asin: Annotated[str, Field(description='Product ASIN for which to get offers. Supports batching of up to 10 ASINs in a single request, separated by comma. Example: B08PPDJWC8,B07ZPKBL9V,B08BHXG144 Note that each ASIN in a batch request is counted as a single request against the plan quota.')],
                   country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                   product_condition: Annotated[Union[str, None], Field(description='Find products in specific conditions, specified as a comma delimited list of the following values: NEW, USED_LIKE_NEW, USED_VERY_GOOD, USED_GOOD, USED_ACCEPTABLE. Default: NEW, USED_LIKE_NEW, USED_VERY_GOOD, USED_GOOD, USED_ACCEPTABLE Examples: NEW,USED_LIKE_NEW USED_VERY_GOOD,USED_GOOD,USED_LIKE_NEW')] = None,
                   delivery: Annotated[Union[str, None], Field(description='Find products with specific delivery option, specified as a comma delimited list of the following values: PRIME_ELIGIBLE,FREE_DELIVERY. Examples: FREE_DELIVERY PRIME_ELIGIBLE,FREE_DELIVERY')] = None,
                   limit: Annotated[Union[int, float, None], Field(description='Maximum number of offers to return. Default: 100 Default: 100')] = None,
                   page: Annotated[Union[int, float, None], Field(description='Results page to return. Default: 1 Default: 1')] = None,
                   language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                   fields: Annotated[Union[str, None], Field(description='A comma separated list of product and offer fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_information,product_condition,ships_from')] = None) -> dict: 
    '''Get all Amazon product details as available via the Product Details endpoint with an additional `offers` array containing product offers (The first offer in the array is the pinned offer returned by the **Search** endpoint). Supports pagination using the `page` and `limit` parameters.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/product-offers'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'asin': asin,
        'country': country,
        'product_condition': product_condition,
        'delivery': delivery,
        'limit': limit,
        'page': page,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seller_profile(seller_id: Annotated[str, Field(description='The Amazon Seller ID for which to get seller profile details')],
                   country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                   language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                   fields: Annotated[Union[str, None], Field(description='A comma separated list of seller profile fields to include in the response (field projection). By default all fields are returned. Example: seller_link,phone,business_name,rating')] = None) -> dict: 
    '''Get Amazon Seller profile details from the Amazon Seller profile page (e.g. https://www.amazon.com/sp?seller=A1D09S7Q0OD6TH).'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/seller-profile'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seller_id': seller_id,
        'country': country,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seller_reviews(seller_id: Annotated[str, Field(description='The Amazon Seller ID for which to get seller reviews')],
                   country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                   star_rating: Annotated[Literal['ALL', '5_STARS', '4_STARS', '3_STARS', '2_STARS', '1_STARS', 'POSITIVE', 'CRITICAL', None], Field(description='Only return reviews with a specific star rating or positive / negative sentiment. Default: ALL Allowed values: ALL, 5_STARS, 4_STARS, 3_STARS, 2_STARS, 1_STARS, POSITIVE, CRITICAL')] = None,
                   page: Annotated[Union[int, float, None], Field(description='The page of seller feedback results to retrieve. Default: 1 Default: 1')] = None,
                   language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                   fields: Annotated[Union[str, None], Field(description='A comma separated list of seller review fields to include in the response (field projection). By default all fields are returned. Example: review_star_rating,review_date')] = None) -> dict: 
    '''Get and paginate through Amazon Seller reviews / feedback as shown on the Seller profile page (e.g. https://www.amazon.com/sp?seller=A1D09S7Q0OD6TH). Each page contains up to 5 reviews.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/seller-reviews'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seller_id': seller_id,
        'country': country,
        'star_rating': star_rating,
        'page': page,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seller_products(seller_id: Annotated[str, Field(description='The Amazon Seller ID for which to get seller product listings')],
                    country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                    page: Annotated[Union[int, float, None], Field(description='The page of seller products results to retrieve Seller products result page to retrieve. Default: 1 Default: 1')] = None,
                    sort_by: Annotated[Literal['RELEVANCE', 'LOWEST_PRICE', 'HIGHEST_PRICE', 'REVIEWS', 'NEWEST', 'BEST_SELLERS', None], Field(description='Return the results in a specific sort order. Default: RELEVANCE Allowed values: RELEVANCE, LOWEST_PRICE, HIGHEST_PRICE, REVIEWS, NEWEST, BEST_SELLERS')] = None,
                    language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                    fields: Annotated[Union[str, None], Field(description='A comma separated list of seller product fields to include in the response (field projection). By default all fields are returned. Example: product_price,product_url,is_prime')] = None) -> dict: 
    '''Get and paginate through the products sold by an Amazon Seller'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/seller-products'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seller_id': seller_id,
        'country': country,
        'page': page,
        'sort_by': sort_by,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def best_sellers(category: Annotated[str, Field(description='Best sellers category to return products for. Supports top level best sellers categories (e.g. software). In addition, subcategories / category path can be specified as well, separated by / (e.g. software/229535) - this can be seen in best sellers URLs, e.g. https://www.amazon.com/Best-Sellers-Software-Business-Office/zgbs/software/229535. Examples: software software/229535')],
                 type: Annotated[Literal['BEST_SELLERS', 'GIFT_IDEAS', 'MOST_WISHED_FOR', 'MOVERS_AND_SHAKERS', 'NEW_RELEASES', None], Field(description='Type of Best Seller list to return. Default: BEST_SELLERS Allowed values: BEST_SELLERS, GIFT_IDEAS, MOST_WISHED_FOR, MOVERS_AND_SHAKERS, NEW_RELEASES')] = None,
                 page: Annotated[Union[str, None], Field(description='Results page to return. Default: 1')] = None,
                 country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                 language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                 fields: Annotated[Union[str, None], Field(description='A comma separated list of product fields to include in the response (field projection). By default all fields are returned. Example: product_title,product_url,product_photo')] = None) -> dict: 
    '''Get Amazon Best Sellers, including prices, ratings, rank and more data points available on Amazon Best Sellers listings. Supports all Amazon Best Seller list types using the `type` parameter: **Best Sellers**, **New Releases**, **Movers & Shakers**, **Most Wished For**, **Gift Ideas**.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/best-sellers'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
        'type': type,
        'page': page,
        'country': country,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def deals(country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
          offset: Annotated[Union[int, float, None], Field(description='Number of results to skip / index to start from (for pagination). Default: 0')] = None,
          categories: Annotated[Union[str, None], Field(description="Return deals with products in specific categories / departments. Multiple categories can be specified as a comma (,) separated list. Numeric category id's can be found in the URL after selecting a specific category on https://www.amazon.com/deals. Examples: 502394 2619525011,2617941011")] = None,
          min_product_star_rating: Annotated[Literal['ALL', '1', '2', '3', '4', None], Field(description='Return deals with products star rating greater than a specific value Default: ALL Allowed values: ALL, 1, 2, 3, 4')] = None,
          price_range: Annotated[Literal['ALL', '1', '2', '3', '4', '5', None], Field(description='Return deals with price within a specific price range. 1 is lowest price range shown on Amazon (e.g. Under $25) while 5 is the highest price range (e.g. $200 & Above). Default: ALL Allowed values: ALL, 1, 2, 3, 4, 5')] = None,
          discount_range: Annotated[Literal['ALL', '1', '2', '3', '4', '5', None], Field(description='Return deals with discount within a specific discount range. 1 is lowest discount range shown on Amazon (e.g. 10% off or more) while 5 is the highest discount range (e.g. 70% off or more). Default: ALL Allowed values: ALL, 1, 2, 3, 4, 5')] = None,
          brands: Annotated[Union[str, None], Field(description='Return deals with products by specific brands. Multiple brands can be specified separated by comma (,). In addition, brand names can be found under the Brand filter on the filter/refinements panel on https://www.amazon.com/deals (when applicable). Examples: AQUA CREST Daixers,Antarctic Star')] = None,
          prime_early_access: Annotated[Union[bool, None], Field(description='Only return prime early access deals.')] = None,
          prime_exclusive: Annotated[Union[bool, None], Field(description='Only return prime exclusive deals.')] = None,
          lightning_deals: Annotated[Union[bool, None], Field(description='Only return lightning deals')] = None,
          language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
          fields: Annotated[Union[str, None], Field(description='A comma separated list of deal fields to include in the response (field projection). By default all fields are returned. Example: deal_type,deal_title,deal_ends_at,savings_amount')] = None) -> dict: 
    '''Get Amazon Deals (Today's Deals / Top Deals, Best Deals, and Lightning Deals) with support for all deal types, filters, and options available on Amazon.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/deals-v2'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'offset': offset,
        'categories': categories,
        'min_product_star_rating': min_product_star_rating,
        'price_range': price_range,
        'discount_range': discount_range,
        'brands': brands,
        'prime_early_access': prime_early_access,
        'prime_exclusive': prime_exclusive,
        'lightning_deals': lightning_deals,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def deal_products(deal_id: Annotated[str, Field(description='Deal ID of the deal to fetch')],
                  country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                  sort_by: Annotated[Literal['FEATURED', 'LOWEST_PRICE', 'HIGHEST_PRICE', 'REVIEWS', 'NEWEST', 'BEST_SELLERS', None], Field(description='Return products in a specific order. Default: FEATURED Allowed values: FEATURED, LOWEST_PRICE, HIGHEST_PRICE, REVIEWS, NEWEST, BEST_SELLERS')] = None,
                  page: Annotated[Union[int, float, None], Field(description='Results page to return. Default: 1 Default: 1')] = None,
                  language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                  fields: Annotated[Union[str, None], Field(description='A comma separated list of deal product fields to include in the response (field projection). By default all fields are returned. Example: product_title,deal_price,deal_badge')] = None) -> dict: 
    '''Get the products of a specific deal by Deal ID. Supports pagination using the *page* parameter. For now, only works for MULTI_ITEM deals with no canonical_deal_url (i.e. when deal_url is in the form of *https://amazon_domain/deal/deal_id*).'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/deal-products'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'deal_id': deal_id,
        'country': country,
        'sort_by': sort_by,
        'page': page,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def promo_code_details(promo_code: Annotated[str, Field(description='Promo code for which to get products. The promo code can be extracted from the /promocode Amazon URL. For example the promo code for https://www.amazon.com/promocode/A31M10S4V50SOU is A31M10S4V50SOU.')],
                       country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                       language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None) -> dict: 
    '''Get the products offered by an Amazon promo code.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/promo-code-details'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'promo_code': promo_code,
        'country': country,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def influencer_profile(influencer_name: Annotated[str, Field(description='The Amazon Influencer name for which to get profile details')],
                       country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                       fields: Annotated[Union[str, None], Field(description='A comma separated list of influencer profile fields to include in the response (field projection). By default all fields are returned. Example: name,profile_link,posts_count,facebook_url')] = None,
                       language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None) -> dict: 
    '''Get Amazon Influencer profile details from the Amazon Influencer store page (e.g. https://www.amazon.com/shop/tastemade).'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/influencer-profile'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'influencer_name': influencer_name,
        'country': country,
        'fields': fields,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def influencer_posts(influencer_name: Annotated[str, Field(description='The Amazon Influencer name for which to get posts')],
                     country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None,
                     scope: Annotated[Literal['ALL', 'IDEA_LISTS', 'PHOTOS', 'VIDEOS', None], Field(description='Return the results in a specific scope. Default: ALL Allowed values: ALL, IDEA_LISTS, PHOTOS, VIDEOS')] = None,
                     query: Annotated[Union[str, None], Field(description='Find posts matching a search query.')] = None,
                     cursor: Annotated[Union[str, None], Field(description='A cursor to get the next set of results, it can be used for for paging purposes. Note: the cursor value for the next set of results is returned by this endpoint under data.cursor.')] = None,
                     limit: Annotated[Union[int, float, None], Field(description='Maximum number of posts to return. Default: 20 Allowed values: 1-100 Default: 20')] = None,
                     language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None,
                     fields: Annotated[Union[str, None], Field(description='A comma separated list of influencer post fields to include in the response (field projection). By default all fields are returned. Example: post_url,post_title,is_pinned,video_duration')] = None) -> dict: 
    '''Get all Amazon Influencer posts with pagination support.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/influencer-posts'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'influencer_name': influencer_name,
        'country': country,
        'scope': scope,
        'query': query,
        'cursor': cursor,
        'limit': limit,
        'language': language,
        'fields': fields,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def influencer_post_products(influencer_name: Annotated[str, Field(description='')],
                             post_id: Annotated[str, Field(description='Influencer Post ID (e.g. amzn1.ideas.1N84PQ3CI4NW0) of the list post for which to get product items (only posts with post_type=List are allowed).')],
                             cursor: Annotated[Union[str, None], Field(description='Set the cursor value from the response of the previous call to get the next results page.')] = None,
                             language: Annotated[Union[str, None], Field(description='The language of the results. In case not specified, results will be returned in the default domain language. Supported languages per country: US: en_US, es_US AU: en_AU BR: pt_BR CA: en_CA, fr_CA FR: fr_FR, en_GB DE: de_DE, en_GB, cs_CZ, nl_NL, pl_PL, tr_TR, da_DK IN: en_IN, hi_IN, ta_IN, te_IN, kn_IN, ml_IN, bn_IN, mr_IN IT: it_IT, en_GB MX: es_MX NL: nl_NL, en_GB SG: en_SG ES: es_ES, pt_PT, en_GB TR: tr_TR AE: en_AE, ar_AE GB: en_GB JP: ja_JP, en_US, zh_CN SA: ar_AE, en_AE PL: pl_PL SE: sv_SE, en_GB BE: fr_BE, nl_BE, en_GB EG: ar_AE, en_AE')] = None) -> dict: 
    '''Get the list of products related to a "List" type post by Post ID.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/influencer-post-products'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'influencer_name': influencer_name,
        'post_id': post_id,
        'cursor': cursor,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def asinto_gtin(asin: Annotated[str, Field(description='Amazon product ASIN to convert.')],
                country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None) -> dict: 
    '''Convert an Amazon ASIN to GTIN / EAN / UPS identifiers. Valid values for `type` are `EAN-13`, `UPC`, or `ISBN`.'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/asin-to-gtin'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'asin': asin,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def product_category_list(country: Annotated[Union[str, None], Field(description='Sets the Amazon domain, marketplace country, language and currency. Default: US Allowed values: US, AU, BR, CA, CN, FR, DE, IN, IT, MX, NL, SG, ES, TR, AE, GB, JP, SA, PL, SE, BE, EG')] = None) -> dict: 
    '''Get Amazon product categories per country / Amazon domain (for use with the "category_id" parameter of the Product Search only).'''
    url = 'https://real-time-amazon-data.p.rapidapi.com/product-category-list'
    headers = {'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
