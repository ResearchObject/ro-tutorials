# Tutorial #01: Creating a Research Object

This is a developer tutorial for creating and consuming [Research Objects](http://www.researchobject.org/).
This tutorial is programming language-agnostic, but assumes some
general [JSON](http://json.org/) and Linux/UNIX shell knowledge.  
(Translating shell commands to Windows Powershell equivalent is left as an exercise for the reader.)


*Status*: **ROUGH DRAFT**: As of 2015-06-23, this document is a *rough draft* in progress. Feel free to help 
**improve** by providing [bugs/wishes/suggestions](https://github.com/ResearchObject/ro-tutorials/issues) and 
[changes](https://github.com/ResearchObject/ro-tutorials/pulls).

*License*: [BSD 2-clause](http://opensource.org/licenses/BSD-2-Clause) - see [LICENSE](../LICENSE) for details.

*Authors*: [Stian Soiland-Reyes](http://orcid.org/0000-0001-9842-9718), 
[Norman Morrison](http://www.cs.manchester.ac.uk/about-us/staff/profile/?ea=Norman.Morrison), 
[Finn Bacall](http://orcid.org/0000-0002-0048-3300)


## Overview

[Research Object](http://www.researchobject.org/) aim to improve reuse and reproducibility in academic scholarship by capturing not just the publication, but also the data and code that support it, in addition to metadata, provenance and detailed annotations about the constituent resources. This extends beyond the traditional "Supplementary resources" as it makes all of those resources first-class citizens and connect them to each other structurally.

The core [Research Object principles](http://www.researchobject.org/overview/) are:

**Identity**: Use globally unique identifiers as names for things

**Aggregation**: Use some mechanism of aggregation to associate things that are related or part of the broader investigation, study, etc. 

**Annotation**: Provide additional metadata about those things, how they relate to each other, where they came from, when etc. 


In this tutorial we'll walk through how to make a simple Research Object, and hopefully along the way show how to achieve each of these principles. 


## Use case: Publishing data and analysis script

Our use case for the purpose of this tutorial is to publish a Research Object that captures the data and analysis scripts that supports an accepted academic paper. We believe this kind of use case occur in many sciences and research fields, obviously with domain-specific variations and additional requirements. 

In this use case, the purpose of the research object is to provide evidence for the claims in the article, but also to provide a direct starting point for someone else who want to reuse the algorithm or raw data.

Conceptually this particular research object should therefore *aggregate* minimally these resources:

* The accepted article
* The raw data
* The analysis script that used the data

A software tool or researcher that pick up the produced research object should be able to understand or use:

* The script performs a particular analysis
* The data was consumed by the script
* The paper is supported by the data and running of the script

## Implementation choices

At the core, [Research Object](http://www.researchobject.org/specifications/) (RO) is a model and vocabulary for describing an aggregation of resources that form part of a larger whole. To realize this model, however, some technology choices also
needs to be done.

While the RO model in theory can be implemented by anything from an [Excel spreadsheet](http://www.researchobject.org/initiative/rightfield/) to a [virtual machine image](http://www.researchobject.org/initiative/docker)/http://www.researchobject.org/initiative/docker/, in practice the choice stands between two approaches:

* [Linked Data](http://www.w3.org/standards/semanticweb/data) on the web  - a series of HTTP accessible resources with links to relate each-other
* [Research Object Bundle](http://www.researchobject.org/initiative/ro-bundle-zip/) - a self-contained research object as a ZIP-file

Each of these have their strengths and weaknesses that we'll cover in detail. 

## Aggregation

At the core of a Research Object is the _aggregation_ of the related resources.
In this example, the three resources to aggregate are available as individual
files:

* [`rawdata5.csv`](rawdata5.csv)
* [`analyse2.py`](analyse2.py)
* [`paper3.pdf`](paper3.pdf)


### Aggregating within an RO Bundle

In the RO Bundle approach, we can add these three files to a ZIP file with our chosen filenames. The RO Bundle specification has one [additional requirement](https://w3id.org/bundle/#ucf) for a special file `mimetype`, that must be the first file in the ZIP file to indicate it is a Research Object. In the shell we can create such a ZIP file like this:

```bash
echo -n application/vnd.wf4ever.robundle+zip > mimetype
zip -0 -X example.bundle.zip mimetype
```

Alternatively you may use the [empty.bundle.zip](empty.bundle.zip) as a starting point:

```bash
cp empty.bundle.zip example.bundle.zip 
```

Adding the files to aggregate to the ZIP:

```bash
zip example.bundle.zip rawdata5.csv paper3.pdf analyse2.py
```

A Research Object Bundle must also include a [manifest](https://w3id.org/bundle/#manifest-json) that declares the aggregated
resources and optionally their metadata. The the manifest is named [`.ro/manifest.json`](.ro/manifest.json), and is in 
[JSON](http://json.org/) format.

A minimal manifest for our example would be:

```json
{ "@id": "/",
  "@context": ["https://w3id.org/bundle/context"],
  "aggregates": [
    "/rawdata5.csv",
    "/paper3.pdf",
    "/analyse2.py"
  ]
}
```

Do not change the `@id` and `@context` from the above values.

Note that the `aggregates` filenames are listed as relative URIs within the ZIP file, 
and should start with `/` with any special characters like space must 
in the manifest 
[%-escaped](https://researchobject.github.io/specifications/bundle/#escaping)
appropriately.

You can now add the manifest to the RO bundle:

```bash
zip example.bundle.zip .ro/manifest.json 
```

`example.bundle.zip` is now a complete minimal Research Object Bundle for the above resources. 
The later sections will show how we can augment this with additional metadata to differentiate
it from a plain ZIP file.


### Aggregating as Linked Data

In the alternative _Linked Data_ approach there is no single file to download the complete Research Object. Instead
the manifest will have to link to resources that can be adressed with a _URI_, typically starting with `http://` or `https://`, 
and itself be published on the web.

So the first step is to ensure we have made our resources available on the web. For simplicity of this tutorial, 
we naively use the URIs at GitHub, but any accessible URI would be valid. (see [identity section](#Identity)).

* https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/analyse2.py
* https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/rawdata5.csv
* https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/paper3.pdf 

A minimal Research Object manifest in [JSON-LD](http://json-ld.org/) that aggregates these 
would look like this:

```json
{ "@id": "#ro",
  "@context": ["https://w3id.org/bundle/context"],
  "aggregates": [
    "https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/rawdata5.csv",
    "https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/paper3.pdf",
    "https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/analyse2.py"
  ]
}
```

If we provide such a JSON file on the web, and ideally make its Content-Type be `application/ld+json`, we have created
Linked Data. The above example has been published as
[https://rawgit.com/ResearchObject/ro-tutorials/master/01-creating/ro.jsonld#ro](https://rawgit.com/ResearchObject/ro-tutorials/master/01-creating/ro.jsonld#ro) which is a valid Resarch Object as Linked Data, and thus its manifest can also be [converted to other RDF formats](http://rdf.greggkellogg.net/distiller?format=turtle&in_fmt=jsonld&uri=https://rawgit.com/ResearchObject/ro-tutorials/master/01-creating/ro.jsonld#ro), if so desired.

_Note_: The `@id` above was set to `#ro` to distinguish the Research Object from its particular manifest as JSON-LD. Other mechanisms include setting the `@id` to absolute URI which on retrieval do a HTTP `303 See Other` redirect to a separate URI for the JSON-LD manifest, often through a permalink service like [w3id.org](https://w3id.org/) or [purl.org](http://purl.org/).


## Identity

**TODO**


## Annotations
.. and provenance

**TODO**


Links:

* http://purl.org/pav/html
* http://www.w3.org/TR/prov-primer/
