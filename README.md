# bedrock_example
Simple example using AWS Bedrock

## Pre-reqs
1. Ensure you have enabled models in AWS for Amazon Bedrock
1. Ensure you have your AWS keys setup in the environment

## Getting Started
1. `python -m venv env`
1. `source env/bin/activate`
1. `pip install -r ./requiremens.txt`

## Example-#1 Running with anthropic.claude-3-5-sonnet-20240620-v1:0

        $ time ./main.py 
        /Users/jmatthews/git/jwmatthews/bedrock_example/env/lib/python3.12/site-packages/langchain_core/_api/deprecation.py:139: LangChainDeprecationWarning: The class `BedrockChat` was deprecated in LangChain 0.0.34 and will be removed in 0.3. An updated version of the class exists in the langchain-aws package and should be used instead. To use it run `pip install -U langchain-aws` and import as `from langchain_aws import ChatBedrock`.
        warn_deprecated(
        /Users/jmatthews/git/jwmatthews/bedrock_example/env/lib/python3.12/site-packages/langchain_core/_api/deprecation.py:139: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use RunnableSequence, e.g., `prompt | llm` instead.
        warn_deprecated(
        Here's a design for a software system that creates a REST API to return the latest stock price for a given ticker symbol using Quarkus:

        ## Specification of the system

        The system will:
        1. Provide a REST endpoint that accepts a ticker symbol as a path parameter
        2. Fetch the latest stock price for the given ticker symbol from a third-party API (e.g., Alpha Vantage)
        3. Return the stock price information in JSON format
        4. Use Quarkus as the framework for building the REST API
        5. Implement caching to improve performance and reduce API calls to the third-party service
        6. Include error handling for invalid ticker symbols or API failures

        ## Summary of what and how this system will function

        The system will be a Quarkus-based REST API that exposes an endpoint `/stock/{symbol}` where `{symbol}` is the ticker symbol of the stock. When a GET request is made to this endpoint, the system will:

        1. Check if the stock price for the given symbol is available in the cache
        2. If cached, return the cached price
        3. If not cached, make a request to the Alpha Vantage API to fetch the latest stock price
        4. Parse the response from Alpha Vantage
        5. Cache the result for a short period (e.g., 5 minutes)
        6. Return the stock price information as a JSON response

        The system will use Quarkus' RESTEasy extension for creating the REST endpoint, the REST Client for making HTTP requests to the Alpha Vantage API, and the Cache extension for implementing caching.

        ## Source code of the system

        Here's the source code for the main components of the system:

        1. `StockResource.java` - The REST endpoint:

        ```java
        package com.example;

        import javax.inject.Inject;
        import javax.ws.rs.GET;
        import javax.ws.rs.Path;
        import javax.ws.rs.PathParam;
        import javax.ws.rs.Produces;
        import javax.ws.rs.core.MediaType;

        import org.jboss.resteasy.annotations.jaxrs.PathParam;

        @Path("/stock")
        public class StockResource {

            @Inject
            StockService stockService;

            @GET
            @Path("/{symbol}")
            @Produces(MediaType.APPLICATION_JSON)
            public StockPrice getStockPrice(@PathParam String symbol) {
                return stockService.getLatestStockPrice(symbol);
            }
        }
        ```

        2. `StockService.java` - The service layer:

        ```java
        package com.example;

        import javax.enterprise.context.ApplicationScoped;
        import javax.inject.Inject;

        import io.quarkus.cache.CacheResult;

        @ApplicationScoped
        public class StockService {

            @Inject
            AlphaVantageClient alphaVantageClient;

            @CacheResult(cacheName = "stock-cache")
            public StockPrice getLatestStockPrice(String symbol) {
                return alphaVantageClient.getStockPrice(symbol);
            }
        }
        ```

        3. `AlphaVantageClient.java` - The REST client for Alpha Vantage API:

        ```java
        package com.example;

        import javax.ws.rs.GET;
        import javax.ws.rs.Path;
        import javax.ws.rs.QueryParam;

        import org.eclipse.microprofile.rest.client.inject.RegisterRestClient;

        @Path("/query")
        @RegisterRestClient(configKey = "alpha-vantage-api")
        public interface AlphaVantageClient {

            @GET
            StockPrice getStockPrice(@QueryParam("function") String function,
                                    @QueryParam("symbol") String symbol,
                                    @QueryParam("apikey") String apiKey);
        }
        ```

        4. `StockPrice.java` - The data model:

        ```java
        package com.example;

        public class StockPrice {
            private String symbol;
            private double price;
            private String lastUpdated;

            // Getters and setters
        }
        ```

        5. `application.properties` - Configuration:

        ```properties
        quarkus.rest-client."alpha-vantage-api".url=https://www.alphavantage.co
        quarkus.rest-client."alpha-vantage-api".scope=javax.
        ./main.py  0.88s user 1.96s system 13% cpu 20.850 total


## Example-2 - similar to Example-1, just re-ran 

        $ time ./main.py 
        /Users/jmatthews/git/jwmatthews/bedrock_example/env/lib/python3.12/site-packages/langchain_core/_api/deprecation.py:139: LangChainDeprecationWarning: The class `BedrockChat` was deprecated in LangChain 0.0.34 and will be removed in 0.3. An updated version of the class exists in the langchain-aws package and should be used instead. To use it run `pip install -U langchain-aws` and import as `from langchain_aws import ChatBedrock`.
        warn_deprecated(
        /Users/jmatthews/git/jwmatthews/bedrock_example/env/lib/python3.12/site-packages/langchain_core/_api/deprecation.py:139: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use RunnableSequence, e.g., `prompt | llm` instead.
        warn_deprecated(
        Here's a design for a software system that creates a REST API to return the latest stock price for a given ticker symbol using Quarkus:

        ## Specification of the system

        The system will:
        1. Provide a REST endpoint that accepts a ticker symbol as a path parameter
        2. Fetch the latest stock price for the given ticker symbol from a third-party API (e.g., Alpha Vantage)
        3. Return the stock price information in JSON format
        4. Use Quarkus as the framework for building the REST API
        5. Implement caching to improve performance and reduce API calls to the third-party service
        6. Include error handling for invalid ticker symbols or API failures

        ## Summary of what and how this system will function

        The system will be a Quarkus-based REST API that exposes an endpoint `/stock/{symbol}` where `{symbol}` is the ticker symbol of the stock. When a GET request is made to this endpoint, the system will:

        1. Check if the stock price for the given symbol is available in the cache
        2. If cached, return the cached price
        3. If not cached, make a request to the Alpha Vantage API to fetch the latest stock price
        4. Parse the response from Alpha Vantage
        5. Cache the result for a short period (e.g., 5 minutes)
        6. Return the stock price information as a JSON response

        The system will use Quarkus' RESTEasy extension for creating the REST endpoint, the REST Client for making HTTP requests to the Alpha Vantage API, and the Cache extension for implementing caching.

        ## Source code of the system

        Here's the source code for the main components of the system:

        1. `StockResource.java` - The REST endpoint:

        ```java
        package com.example;

        import javax.inject.Inject;
        import javax.ws.rs.GET;
        import javax.ws.rs.Path;
        import javax.ws.rs.PathParam;
        import javax.ws.rs.Produces;
        import javax.ws.rs.core.MediaType;

        import org.jboss.resteasy.annotations.jaxrs.PathParam;

        @Path("/stock")
        public class StockResource {

            @Inject
            StockService stockService;

            @GET
            @Path("/{symbol}")
            @Produces(MediaType.APPLICATION_JSON)
            public StockPrice getStockPrice(@PathParam String symbol) {
                return stockService.getLatestStockPrice(symbol);
            }
        }
        ```

        2. `StockService.java` - The service layer:

        ```java
        package com.example;

        import javax.enterprise.context.ApplicationScoped;
        import javax.inject.Inject;

        import io.quarkus.cache.CacheResult;

        @ApplicationScoped
        public class StockService {

            @Inject
            AlphaVantageClient alphaVantageClient;

            @CacheResult(cacheName = "stock-cache")
            public StockPrice getLatestStockPrice(String symbol) {
                return alphaVantageClient.getStockPrice(symbol);
            }
        }
        ```

        3. `AlphaVantageClient.java` - The REST client for Alpha Vantage API:

        ```java
        package com.example;

        import javax.ws.rs.GET;
        import javax.ws.rs.Path;
        import javax.ws.rs.QueryParam;

        import org.eclipse.microprofile.rest.client.inject.RegisterRestClient;

        @Path("/query")
        @RegisterRestClient(configKey = "alpha-vantage-api")
        public interface AlphaVantageClient {

            @GET
            StockPrice getStockPrice(@QueryParam("function") String function,
                                    @QueryParam("symbol") String symbol,
                                    @QueryParam("apikey") String apiKey);
        }
        ```

        4. `StockPrice.java` - The data model:

        ```java
        package com.example;

        public class StockPrice {
            private String symbol;
            private double price;
            private String lastUpdated;

            // Getters and setters
        }
        ```

        5. `application.properties` - Configuration:

        ```properties
        quarkus.rest-client."alpha-vantage-api".url=https://www.alphavantage.co
        quarkus.rest-client."alpha-vantage-api".scope=javax.
        ./main.py  0.88s user 1.96s system 13% cpu 20.850 total
        (env) [jmatthews] in ~/git/jwmatthews/bedrock_example (main) $ time ./main.py
        /Users/jmatthews/git/jwmatthews/bedrock_example/env/lib/python3.12/site-packages/langchain_core/_api/deprecation.py:139: LangChainDeprecationWarning: The class `BedrockChat` was deprecated in LangChain 0.0.34 and will be removed in 0.3. An updated version of the class exists in the langchain-aws package and should be used instead. To use it run `pip install -U langchain-aws` and import as `from langchain_aws import ChatBedrock`.
        warn_deprecated(
        /Users/jmatthews/git/jwmatthews/bedrock_example/env/lib/python3.12/site-packages/langchain_core/_api/deprecation.py:139: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use RunnableSequence, e.g., `prompt | llm` instead.
        warn_deprecated(
        Sure, I'd be happy to design a software system for a REST API that returns the latest stock price for a given ticker symbol using Quarkus. Here's the design:

        ## Specification of the system

        The system will be a Quarkus-based REST API with the following characteristics:
        1. A single endpoint that accepts a ticker symbol as a path parameter
        2. The endpoint will return the latest stock price for the given ticker symbol
        3. Stock data will be fetched from a third-party API (for this example, we'll use Alpha Vantage)
        4. The system will use Quarkus' RESTEasy reactive for handling HTTP requests
        5. We'll use the REST Client to interact with the external API
        6. Caching will be implemented to reduce the number of calls to the external API

        ## Summary of what and how this system will function

        The system will function as follows:
        1. When a GET request is made to the endpoint (e.g., `/stock/{symbol}`), the system will first check if the stock price for the given symbol is cached.
        2. If the price is cached and not expired, it will return the cached price.
        3. If the price is not cached or the cache has expired, the system will make a call to the Alpha Vantage API to fetch the latest stock price.
        4. The fetched price will be cached and then returned to the client.
        5. The system will use Quarkus' built-in caching mechanism for efficient data storage and retrieval.

        ## Source code of the system

        Here's the source code for the system:

        1. First, let's create the `pom.xml` file with the necessary dependencies:

        ```xml
        <?xml version="1.0"?>
        <project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <modelVersion>4.0.0</modelVersion>
        <groupId>com.example</groupId>
        <artifactId>stock-price-api</artifactId>
        <version>1.0.0-SNAPSHOT</version>
        <properties>
            <compiler-plugin.version>3.8.1</compiler-plugin.version>
            <maven.compiler.parameters>true</maven.compiler.parameters>
            <maven.compiler.source>11</maven.compiler.source>
            <maven.compiler.target>11</maven.compiler.target>
            <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
            <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
            <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>
            <quarkus.platform.group-id>io.quarkus.platform</quarkus.platform.group-id>
            <quarkus.platform.version>2.9.2.Final</quarkus.platform.version>
            <surefire-plugin.version>3.0.0-M5</surefire-plugin.version>
        </properties>
        <dependencyManagement>
            <dependencies>
            <dependency>
                <groupId>${quarkus.platform.group-id}</groupId>
                <artifactId>${quarkus.platform.artifact-id}</artifactId>
                <version>${quarkus.platform.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            </dependencies>
        </dependencyManagement>
        <dependencies>
            <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-resteasy-reactive</artifactId>
            </dependency>
            <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-rest-client-reactive</artifactId>
            </dependency>
            <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-rest-client-
        ./main.py  1.74s user 1.52s system 17% cpu 19.025 total

