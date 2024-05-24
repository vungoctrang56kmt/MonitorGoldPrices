use GoldPrices
CREATE TABLE GoldPrices (
    timestamp BIGINT,
    metal VARCHAR(10),
    currency VARCHAR(10),
    exchange VARCHAR(50),
    symbol VARCHAR(50),
    prev_close_price FLOAT,
    open_price FLOAT,
    low_price FLOAT,
    high_price FLOAT,
    open_time BIGINT,
    price FLOAT,
    ch FLOAT,
    chp FLOAT,
    ask FLOAT,
    bid FLOAT,
    price_gram_24k FLOAT,
    price_gram_22k FLOAT,
    price_gram_21k FLOAT,
    price_gram_20k FLOAT,
    price_gram_18k FLOAT,
    price_gram_16k FLOAT,
    price_gram_14k FLOAT,
    price_gram_10k FLOAT
);

CREATE PROCEDURE InsertGoldPrice
    @timestamp BIGINT,
    @metal VARCHAR(10),
    @currency VARCHAR(10),
    @exchange VARCHAR(50),
    @symbol VARCHAR(50),
    @prev_close_price FLOAT,
    @open_price FLOAT,
    @low_price FLOAT,
    @high_price FLOAT,
    @open_time BIGINT,
    @price FLOAT,
    @ch FLOAT,
    @chp FLOAT,
    @ask FLOAT,
    @bid FLOAT,
    @price_gram_24k FLOAT,
    @price_gram_22k FLOAT,
    @price_gram_21k FLOAT,
    @price_gram_20k FLOAT,
    @price_gram_18k FLOAT,
    @price_gram_16k FLOAT,
    @price_gram_14k FLOAT,
    @price_gram_10k FLOAT
AS
BEGIN
    INSERT INTO GoldPrices (
        timestamp, metal, currency, exchange, symbol,
        prev_close_price, open_price, low_price, high_price, open_time,
        price, ch, chp, ask, bid,
        price_gram_24k, price_gram_22k, price_gram_21k,
        price_gram_20k, price_gram_18k, price_gram_16k,
        price_gram_14k, price_gram_10k
    ) VALUES (
        @timestamp, @metal, @currency, @exchange, @symbol,
        @prev_close_price, @open_price, @low_price, @high_price, @open_time,
        @price, @ch, @chp, @ask, @bid,
        @price_gram_24k, @price_gram_22k, @price_gram_21k,
        @price_gram_20k, @price_gram_18k, @price_gram_16k,
        @price_gram_14k, @price_gram_10k
    );
END;

