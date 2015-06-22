# Tutorial #01: Creating a Research Object

This is a developer tutorial for creating and consuming [Research Objects](http://www.researchobject.org/).
This tutorial is programming language-agnostic, but assumes some
generalk [JSON](http://json.org/) and shell knowledge.  

*Status*: **ROUGH DRAFT**: As of 2015-06-22, this document is a *rough draft* in progress. Feel free to help 
**improve** by providing [bugs/wishws/suggestions](https://github.com/ResearchObject/ro-tutorials/issues) and 
[changes](https://github.com/ResearchObject/ro-tutorials/pulls).

*License*: [BSD 2-clause](http://opensource.org/licenses/BSD-2-Clause) - see [LICENSE](../LICENSE)

*Authors*: [Stian Soiland-Reyes](http://orcid.org/0000-0001-9842-9718), [Norman Morrison](http://www.cs.manchester.ac.uk/about-us/staff/profile/?ea=Norman.Morrison)


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

## Implementations

At the core, [Research Object](http://www.researchobject.org/specifications/) (RO) is a model and vocabulary for describing an aggregation of resources that form part of a larger whole. To realize this model, however, some technology choices also
needs to be done.

While the RO model in theory can be implemented by anything from an [Excel spreadsheet](http://www.researchobject.org/initiative/rightfield/) to a [virtual machine image](http://www.researchobject.org/initiative/docker)/http://www.researchobject.org/initiative/docker/, in practice the choice stands between two approaches:

* [Linked Data](http://www.w3.org/standards/semanticweb/data) on the web  - a series of HTTP accessible resources with links to relate each-other
* [Research Object Bundle](http://www.researchobject.org/initiative/ro-bundle-zip/) - a self-contained research object as a ZIP-file


## Aggregation
**TODO**

## Identity
**TODO**

## Annotations
.. and provenance

**TODO**


Links:

* http://purl.org/pav/html
* http://www.w3.org/TR/prov-primer/
