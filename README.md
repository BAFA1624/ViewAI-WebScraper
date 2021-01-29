# ViewAI-WebScraper
<p>Repo for the development of the web scraping element of ViewAI using AWS</p>


## Schema files & Configuration Files
----------------------------------

#### For detailed info on schema, visit https://json-schema.org/understanding-json-schema/ or https://json-schema.org/understanding-json-schema/UnderstandingJSONSchema.pdf

### Schema:
<p>JSON Schema is a powerful tool for validating the structure of JSON (Javascript Object Notation) data.
It uses various key words to allow a developer to selectively allow or restrict many properies of JSON objects, for example allowed data types, number of objects, required data, are additional arguments allowed, the list goes on.</p>
<p>As of 29/01/21, the default schema is as follows:</p>

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

<p>But what does this mean? The "<b>type</b>" tag</p>


