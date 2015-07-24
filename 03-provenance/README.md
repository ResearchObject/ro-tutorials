# Tutorial 3: Provenance of a Research Object

This is part of [developer tutorials](../) for creating and consuming
[Research Objects](http://www.researchobject.org/) (RO).
This tutorial is programming language-agnostic, but assumes some
general [JSON](http://json.org/) and Linux/UNIX shell knowledge.
(Translating shell commands to Windows PowerShell equivalent is left as an exercise for the reader.)


*Status*: **ROUGH DRAFT**: As of 2015-06-23, this document is a *rough draft* in progress. Feel free to help
**improve** by providing [bugs/wishes/suggestions](https://github.com/ResearchObject/ro-tutorials/issues) and
[changes](https://github.com/ResearchObject/ro-tutorials/pulls).

*License*: [BSD 2-clause](http://opensource.org/licenses/BSD-2-Clause) - see [LICENSE](../LICENSE) for details.

*Authors*: [Stian Soiland-Reyes](http://orcid.org/0000-0001-9842-9718),
[Norman Morrison](http://www.cs.manchester.ac.uk/about-us/staff/profile/?ea=Norman.Morrison),
[Finn Bacall](http://orcid.org/0000-0002-0048-3300)


## Previous step

This tutorial assumes you have already completed the previous
[tutorial on identity of ROs](../02-identity/).

## Provenance

A Research Object often combines resources that have diverse set of authord
and history. Tracking the provenance of the resources and the RO itself
supports their authenticity and traceability, and gives authors
and contributors credit for their individual works.

In Research Objects, there are several provisions for tracking provenance:

1. In the manifest on a per-resource basis
2. In annotations, connecting related resources
3. In a separate provenance trace (e.g. log of a workflow run)

The RO Bundle specifications provides a selection of
[common provenance attributes](https://w3id.org/#provenance) which
can be used directly within the manifest.

Perhaps the most important aspect to record in any research object is the
creation of the RO itself:

```json
{
  "@context": ["https://w3id.org/bundle/context"],
  "@id": "/",
  "createdOn": "2015-06-24T08:05:00+0100",
  "createdBy": {
    "name": "John Doe",
  },
  "aggregates": [  
    ".."
  ]
}
```

RO Bundle relies on the existing
provenance vocabulary [PAV](http://purl.org/pav/html) to
provide the definitions of terms like
[createdOn](http://purl.org/pav/html#http://purl.org/pav/createdOn),
[createdBy](http://purl.org/pav/html#http://purl.org/pav/createdBy), which are
based on the [W3C PROV](http://www.w3.org/TR/prov-primer/) model for provenance
statements.

### Identifying contributors

It is beneficial to also provide a `uri` or `orcid` URI for the person(s) that
created the research object or some of its resources. This helps to
identify and distinguish contributors across resources and research objects.

While providing the `name` is crucial for
presentation purposes, names are often not globally unique, and some people
might have multiple names.

[ORCID](http://orcid.org)s are preferred
as it gives a unique identifier for an academic author across
multiple publication and authorship systems.



```json
{
  "createdBy": {
    "name": "John Doe",
    "orcid": "http://orcid.org/0000-0001-5429-1577"
  }
}
```

_Note: ORCIDs should be provided by the user explicitly
(e.g. by signing in via [orcid.org](http://orcid.org/),
not looked up as a ORCID search with a
full name - that might match the wrong person and
would defy the purpose of uniquely identifying the
contributor._

The `uri` field can be used with any other kind of
[WebId](http://www.w3.org/2005/Incubator/webid/spec/identity/) to identify
the person. In many cases, a system exporting a Research Object will have some
web resource corresponding to the user account, which can easily be used
directly with `uri`, and thus still provide unique identification across
research objects from the same system:

```json
{
  "createdBy": {
    "name": "John Doe",
    "orcid": "http://orcid.org/0000-0001-5429-1577",
    "uri": "http://example.com/user/johnd"
  }
}
```


### Creator, author or contributor?

**TODO**: ...

### Retrieved From

**TODO**:
