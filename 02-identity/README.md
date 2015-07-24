# Tutorial #2: Identity of a Research Object

This is part of [developer tutorials](../) for creating and consuming
[Research Objects](http://www.researchobject.org/) (RO).
This tutorial is programming language-agnostic, but assumes some
general [JSON](http://json.org/) and Linux/UNIX shell knowledge.  
(Translating shell commands to Windows PowerShell equivalent is left as an exercise for the reader.)


*Status*: **DRAFT**: As of 2015-06-23, this document is a *draft* in progress. Feel free to help
**improve** by providing [bugs/wishes/suggestions](https://github.com/ResearchObject/ro-tutorials/issues) and
[changes](https://github.com/ResearchObject/ro-tutorials/pulls).

*License*: [BSD 2-clause](http://opensource.org/licenses/BSD-2-Clause) - see [LICENSE](../LICENSE) for details.

*Authors*: [Stian Soiland-Reyes](http://orcid.org/0000-0001-9842-9718),
[Norman Morrison](http://www.cs.manchester.ac.uk/about-us/staff/profile/?ea=Norman.Morrison),
[Finn Bacall](http://orcid.org/0000-0002-0048-3300)


## Previous step

This tutorial assumes you have completed the
previous [tutorial for creating an RO](../01-creating).


## Identity

It is important to be able to identify a Research Object.
The RO identity serves multiple purposes,
including:

1. To uniquely cite or reference a research object
2. To describe the research object in annotations
3. To relate research objects to each other
4. To retrieve the research object

### Identifying Linked Data Research Objects

A Linked Data Research Object should follow the rules
for [Cool URIs for the Semantic Web](http://www.w3.org/TR/cooluris/).
Making sure your RO manifest is on a stable and platform-neutral URI space is a
good start. If your RO URI looks like
`http://underthedesk5.example.com/wordpress-1.3.2/download.php?attachment=155&action=doit`
you still have some work to do.

In the RO manifest, the top-level `@id` attribute defines the identity of the
described Research Object.
It is important to distinguish URIs for the Research Object and its manifest.
For Linked Data ROs, this is easiest achieved by declaring the `@id`
with a [hash URI](http://www.w3.org/TR/cooluris/#hashuri) like `#ro`, which
would then be a relative URI from where the manifest was retrieved from.

Another solution is to use an absolute URI for that on HTTP retrieval do a
[303 See Other](http://www.w3.org/TR/cooluris/#r303gendocument) redirect to a
separate URI for the JSON-LD manifest, often through a third-party
permalink service like [w3id.org](https://w3id.org/) or
[purl.org](http://purl.org/), which would also give you
future flexibility on the server to host the manifest from.
In this case the manifest should specify the permalink as it's `@id`, e.g.
[http://purl.org/wf4ever/ro-ex2](http://purl.org/wf4ever/ro-ex2)

### Identifying Research Object Bundles

An embedded permalink is often not a good solution for Research Object Bundles.
While [http://purl.org/wf4ever/bundle-ex2](http://purl.org/wf4ever/bundle-ex2)
is probably a good identifier for the RO, if this identifier was also explicitly
mentioned in the embedded manifest, we face some challenges:

1. The identifier must be known before the ZIP file is finished - ruling out
unique hash/commit-like identifiers
2. Two downloads of the ZIP file might claim to be equal, even if one
of them might be a newer version with different content.
3. A user might modify the ZIP file without changing the `@id`

Unless you have control over these aspects, we recommend that you
instead feature  prominently the identifier for the
research object wherever you link to it. This typically means the use
of a persistent identifier and versioning scheme rather than a
`?download`-style link.

A system that is generating a Research Object Bundle on the fly may
however describe which "live" RO it came from, using
[`retrievedFrom`](https://w3id.org/bundle/#retrievedFrom)
and friends:

```json
{ "@id": "/",
  "retrievedFrom": "https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/example.bundle.zip?raw=true",
  "retrievedOn": "2015-06-23T16:24:00+0100",
  "retrievedBy": { "name": "Stian Soiland-Reyes", "orcid": "http://orcid.org/0000-0001-9842-9718" },
  "aggregates": [ "..." ]
}
```

### Where is / in the RO bundle?

A Research Object Bundle discovered "in the wild" can be uniquely identified
by generating a non-resolvable
UUID or SHA-based `app://` URI, as
[detailed in the RO bundle specification](https://w3id.org/bundle/#absolute-uris).

There are three variants, all of which will result in a URI like:

```
app://77a2d494-bbd6-410e-a0cf-d48abd5e0ea9/
```

This would be both an identifier for the Research Object Bundle itself,
but also for the `/` folder of the ZIP file. Thus
a manifest claiming `"@id": "/"` would resolve to the
above absolute URI.

This forms the base URI and can thus be used to identify any resource
in a parsed RO Bundle Zip file, e.g.
`app://77a2d494-bbd6-410e-a0cf-d48abd5e0ea9/analyse2.py`.

Which variant to use to resolve depends on the uniqueness constraints for
the URI and the research object. The _SHA-256 checksum_ of the ZIP-file is useful
for identifying a RO Bundle uniquely based on its binary content, no matter
where it is hosted, but would always give a new identifier for ROs that
are generated on demand (e.g. becaue of timestamps within the ZIP-file),
and still does not take into account any changes of external URIs.

A _location-based UUID_ would be the same for any
RO Bundle downloaded from the same location, even if their content might have
changed. A _random UUID_ is most probably unique in the universe,
and useful for security sandboxing, but have no
direct relation to the Research Object Bundle.


### Identifying aggregated resources

In our research object bundle, we aggregated resources by adding them as files
to the ZIP-file. Using the relative URIs, it is unambiguous that
`/paper3.pdf` refers to the included PDF. This is however less useful if we have
multiple research object bundles, as you would not know immediately that two
research objects refer to the same paper.

Published scientific papers would
typically be assigned a [DOI](http://www.doi.org/), which is commonly used
for citation and identification, and also for resolution using the
[http://dx.doi.org/](http://dx.doi.org/) prefix.

**For items that already are identified by an unambiguous identity,
aggregate using their absolute URI.**

So for both the Research Object Bundle and the Linked Data Research Object,
we'll replace the links to the paper PDFs with a DOI link:

```json
  "aggregates": [
    "http://dx.doi.org/10.5281/zenodo.18877",
    "/rawdata5.csv",
    "/analyse2.py"
  ]
```

### Persistent identifiers

Different research domains may have repositories that are already commonly
used and which assign persistent identifiers. Generic repositories
of research data and software include [figshare](http://figshare.com/)
and [Zenodo](http://zenodo.org/).

It is recommended that "external" URIs aggregated by a research object follow
the
[10 Simple Rules for design, provision and reuse of persistent identifiers for live science data](http://dx.doi.org/10.5281/zenodo.18003)
and are ["Cool URIs"](http://www.w3.org/Provider/Style/URI.html). This includes
ensuring that the URIs don't change and remain available.


### Resources that change

The semantics of aggregating an external URI changes. Rather than
the research object aggregating the actual PDF you would instead be aggregating
the paper in a more abstract sense, and have to rely on the third-party provider
for it to remain available.

For resources that might change over time, this might not be what
you want for your research object. For instance, in our example we have a
[paper](paper3.pdf) that claims that Alice was the one that left the office last,
supported by the data in [rawdata5.csv](rawdata5.csv). If we instead linked to
the original data file as say
[https://drive.google.com/file/d/0B9pchNBBcY-qMThBaHVjUENvY28/view?usp=sharing](https://drive.google.com/file/d/0B9pchNBBcY-qMThBaHVjUENvY28/view?usp=sharing)
we are not just of risk of Google Drive changing that fragile URL syntax
so the data can no longer be accessed, but also that the data itself might
change and no longer be consistent with the paper or the research object.

For "fragile" resources it is best to archive a snapshot
within the Research Object or within your own web space, and rather
express the [provenance](#Provenance) of the file to indicate its history and
other identifiers.

Sometimes it might make sense to aggregate both a snapshot and the live
resource. This could for instance be because you want the consumer of
the research object to understand you mean the current live version
(e.g. allowing for bug fixes), but also want to provide a snapshot
for archival reasons.

```json
"retrievedFrom": "TODO"
```

### Example: GitHub identifiers

In our Linked Data Research Object, we aggregated:

[https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/rawdata5.csv](https://github.com/ResearchObject/ro-tutorials/blob/master/01-creating/rawdata5.csv).

This identifier has several issues:

1. Its content is subject to change (it reflects the current `master` branch)
2. Its syntax might change (e.g. if GitHub stop using `blob/master`)
3. Resolving the identifier presents a HTML rendering of the CSV file with
additional metadata - but the analysis used the raw CSV file, not the
GitHub webpage.

To avoid the content to change, we'll try to use the host's internal
versioning/snapshot features, if it exists. For GitHub this could
be achieved with the git commit identifiers:

[https://github.com/ResearchObject/ro-tutorials/blob/9228550315a6f9a2b969abd19003b5e1ec1837e1/01-creating/rawdata5.csv](https://github.com/ResearchObject/ro-tutorials/blob/9228550315a6f9a2b969abd19003b5e1ec1837e1/01-creating/rawdata5.csv)

To solve #3 we can use the _Raw_ button at GitHub:

[https://raw.githubusercontent.com/ResearchObject/ro-tutorials/9228550315a6f9a2b969abd19003b5e1ec1837e1/01-creating/rawdata5.csv](https://raw.githubusercontent.com/ResearchObject/ro-tutorials/9228550315a6f9a2b969abd19003b5e1ec1837e1/01-creating/rawdata5.csv)

The URIs for raw files on GitHub has changed several times over the last years,
so we can probably not rely on the above still working in the future.
Other repositories may unfortunately have even less reliable URIs for downloads
which may be hard to find, e.g. Dropbox's [web rendering](https://www.dropbox.com/s/yf086tmmjyjpmua/rawdata5.csv?dl=0)
links to the fragile-looking-
[https://dl-web.dropbox.com/get/tmp/rawdata5.csv?_subject_uid=794465&w=AAAJWP3B47gxnuOH-JYC5_OqN9XVw7vR5c1G5yFI0FFS2w&dl=1](https://dl-web.dropbox.com/get/tmp/rawdata5.csv?_subject_uid=794465&w=AAAJWP3B47gxnuOH-JYC5_OqN9XVw7vR5c1G5yFI0FFS2w&dl=1)

For resources on GitHub we can alternatively
use the third-party [rawgit.com](http://rawgit.com/), which
persists a copy of the GitHub file on its content-delivery
network, and also provides the correct Content-Type.

[https://cdn.rawgit.com/ResearchObject/ro-tutorials/9228550315a6f9a2b969abd19003b5e1ec1837e1/01-creating/rawdata5.csv](https://cdn.rawgit.com/ResearchObject/ro-tutorials/9228550315a6f9a2b969abd19003b5e1ec1837e1/01-creating/rawdata5.csv)

Now we have achieved a versioned and unchanging URI that resolves directly
to the CSV and opens nicely in our spreadsheet software.
We have done that at the cost of relying on a third-party
provider.

You will face similar challenges if linking to resources on cloud services
like Dropbox, Google Drive and your own content and data management systems.
The persistency measures you need to take for your research object depends
on the purpose of the RO and the linked resource.

For instance, a Research Object Bundle that is to
be deposited at a publisher as part of a peer-reviewed article
should be constructed so it would still have meaning beyond the lifetime of
cloud services and your own institution's servers. A Research Object that is a
"work in progress" within a Dropbox folder can be more lax and link
directly to "live" resources.


### Restricting access

In some cases, not being able to access a resource is desired. For instance, if
you are creating a research object that also aggregate patient data, you might
want to aggregate those by URIs, which when accessed has a more restrictive
access control and firewalls.

In this way you can publish and distribute your research object
and metadata openly, yet remain in control over access to the sensitive data.


### bundledAs

A research object may also want to assign identifiers for its
bundled resources, using the [bundledAs](https://w3id.org/bundle#manifest-bundledAs)
statement and random [urn:uuid:](http://www.ietf.org/rfc/rfc4122) URIs. This
requires the expanded `{ "uri": ".."} ` form of `aggregates`:

```json
"aggregates": [
    { "uri": "http://dx.doi.org/10.5281/zenodo.18877",
      "bundledAs": { "uri": "urn:uuid:55fd1801-046c-4de3-ac64-f7294bf97b98"}
    },
    { "uri": "/analyse2.py",
      "bundledAs": { "uri": "urn:uuid:3ce09074-9ce6-4b14-b878-f4d1fa4191df"}
    },
    { "uri": "/rawdata5.csv",
      "bundledAs": { "uri": "urn:uuid:c8f5ec32-31b6-47a8-8c8e-6e0e281516b7"}
    }
  ]
}
```

The `bundledAs` identifiers must be unique for each resource in each
research object and kind of represents
"this resource as part of this particular RO".
This is particularly useful for external URIs that may be referenced
from several research objects.

These identifiers might subsequently be used in embedded and external
annotations, e.g. to describe _why_ a particular file is in the Research Object,
or for a third-party to unambiguously _cite_ a resource within your research object.
As `urn:uuid:` URIs, they are however not resolvable, and therefore should also
be accompanied with links to the Research Object Bundle and/or the freestanding
resources.

## Next step:

The next [tutorial on provenance](../03-provenance) details
how to describe who created your resources, and where they came from.
