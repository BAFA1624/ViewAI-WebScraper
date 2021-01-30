# ViewAI-WebScraper
<p>Repo for the development of the web scraping element of ViewAI using AWS</p>


## Schema files & Configuration Files
----------------------------------

#### For detailed info on schema, visit https://json-schema.org/understanding-json-schema/ or https://json-schema.org/understanding-json-schema/UnderstandingJSONSchema.pdf

<p>Both configuration and schema files should be provided in a '.json' format. In the near future there will be a validation program you can use check the validity of any new configuration or schema files.</p>

### Schema:
<p>JSON Schema is a powerful tool for validating the structure of JSON (JavaScript Object Notation) data.
It uses various key words to allow a developer to selectively allow or restrict many properies of JSON objects, for example allowed data types, number of objects, required data, are additional arguments allowed, the list goes on.</p>
<p>As of 29/01/21, the default schema is:</p>
<pre><code>
{
    "type": "object",
    "properties": {
        "tags": {
            "type": "array"
        },
        "attrs": {
            "type": "object"
        },
        "bad-attrs": {
            "type": "object"
        },
        "output-format": {
            "type": "object"
        }
    },
    "required": [
        "tags",
        "attrs",
        "bad-attrs",
        "output-format"
    ],
    "additionalProperties": false
}
</code></pre>
<p>But what does this mean?</p>
<ul>

<li>"<b>type</b>": Defines the allowed object(s) type(s) using JavaScript types. Multiple can be indicated using an array, eg "type": [type1, type2,...]</li>
<li>"<b>properties</b>": "object" type schema are the equivalent of a dictionary in python or hash in many other languages. "properties" are equivalent to the keys in a python dictionary. Notice we are also able to specify their type.</li>
<li>"<b>required</b>": The "required" tag is self-explanatory, it tells the schema which out of the given "properties" MUST be present for it to be valid.</li>
<li>"<b>additionalProperties</b>": "additionalProperties" tells the schema whether an instance(configuration) it is being checked against is allowed to contain additional properties or not.</li>

</ul>

<p>For know only the "tags" and "attrs" properties do anything useful. "bad-attrs" and "output-format" are expected to be necessary for parsing a webpage in WebScraper.soupToText(...), however this is not yet implemented as of 29/01/21.</p>

### Configurations

<p>Configuration files work within a given schema to direct a WebScraper object to gather the intended information from a webpage. Here's an example:</p>

<pre><code>
{
    "tags": [
        "p"
    ],
    "attrs": {
        "data-element": "text-block"
    },
    "bad-attrs": {},
    "output-format": {
        "n_items": 2,
        "item_type": "sentence"
    }
}
</code></pre>

<p>The "tags" property takes an array which contains the tags that the SoupStrainer object created in the WebScraper.soupify(...) will tell BeautifulSoup(...) to parse for. The "attr" property is similar, except it takes an object which specifies attributes within tags to search for. Note, adding many tags and attributes seems to slow down BeautifulSoup notably though more testing needs to be done. While unimplemented, "bad-attrs" will be used to filter out tags which are from unwanted parts of a webpage but share tags or attributes we are already filtering for. "output-format" will be likely become a strictly constrained method to specify how the text is outputted to control the format of the data passed to the S3 bucket supplying the financial model.</p>

