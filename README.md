# ViewAI-WebScraper
<p>Repo for the development of the web scraping element of ViewAI using AWS</p>


## Schema files & Configuration Files
----------------------------------

#### For detailed info on schema, visit https://json-schema.org/understanding-json-schema/ or https://json-schema.org/understanding-json-schema/UnderstandingJSONSchema.pdf

### Schema:
<p>JSON Schema is a powerful tool for validating the structure of JSON (JavaScript Object Notation) data.
It uses various key words to allow a developer to selectively allow or restrict many properies of JSON objects, for example allowed data types, number of objects, required data, are additional arguments allowed, the list goes on.</p>
<p>As of 29/01/21, the default schema is as follows:</p>
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


