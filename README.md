# The Digital _Messkataloge_
#
# An Overview of the _Messkataloge_ Database
by David Kretz and Jeffrey Tharsen

Studies of the history of the book in the early modern German-speaking world have been greatly aided by the creation of national bibliographies, or “VD”s (_Verzeichnis der Druckerzeugnisse_). These exist in limited forms for the 16th, 17th, and 18th century; of these, only the VD for the 17th century can lay a claim to both near-comprehensiveness and digital accessibility, and no current Verzeichnis exists for the 19th century. In recent decades, however, a consortium of German libraries converted the _Messkataloge_ (the printed “book catalogs” created for the Frankfurt and Leipzig book fairs from 1594 to 1860) to microfilm, and then generated PDFs of these catalogs: 536 registers totaling 65,658 pages. 

Due to a lack of machine-readable versions, previous research into the Verzeichnis has dealt with only a few individual catalogs of particular years.  We thus undertook a project building upon the work by German libraries to harness the world’s most advanced Optical Character Recognition (OCR) system and convert all 65,658 pages of the _Messkataloge_ from the original images to machine-readable plaintext, achieving over 98% accuracy and resulting in the first digital database of the _Messkataloge_.  This work has opened up exciting new possibilities, as scholars can now search the data for insights into, for example: where books were published during the formative periods of German publishing,  the rise and fall of particular genres,  of religious writings,  or the declining dominance of Latin,  with a precision hitherto unmatched (particularly for the 19th century).

To aid scholars, librarians, and book historians we also include here a Bokeh-based open-source custom version of Google’s N-Gram Viewer via which one can plot relative and absolute word frequencies over time, determine covariance between terms, and investigate the wealth of data in the _Messkataloge_ for any time period during its production.  As a next step, we plan to develop more precise tools that allow scholars to also group search terms into indices allowing for analyses of complex phenomena over time; for example, the phenomenon of secularization could be analyzed by combining searches for religious terms (e.g. “sermon,” “Catholic,” “Protestant,” “Bible,” “New Testament, “Old Testament” and so on) into one index. Certain biases to the representativeness of the catalogs have contributed to a lack of their consideration in the literature hitherto, and need to be noted: there is a focus on Northern German publishers, especially from Leipzig (which did, however, produce almost as many books as the rest of Germany together in the 18th century), on Protestant over Catholic publishers, on books at the expense of other kinds of printed products, and we find occasional listings for forthcoming books that were ultimately not published.  Comparison with data from the VD17 and VD18 should help correct such biases.

Our ultimate goal is to aid in the production of a critical digital edition of the _Messkataloge_: we are giving the database we have created to the German libraries that began this work to enable scholars and scholarship beyond what we can possibly envision at this point. Many exciting and concrete follow up projects suggest themselves already; we conclude by outlining just one of these in detail.

One prominent follow-up project to the _Messkataloge_ digitization takes its cue from Bachleitner’s call to combine translation studies with book history.  In a first step, we plan to cross-check the data from the _Messkataloge_ with VD17 and VD18 data on translations (relative share of translations over time, in total, by genre, and publication place; relative share of source languages and genres among translations generally). In a second step, we will build a smaller database of translators’ prefaces that faithfully maps larger trends, focusing on the period of 1750-1830 which saw a revolution in translation theory and praxis.  This new research situates itself in relation to the existing research programmes inquiring into “small forms”  to empower scholars to examine the genesis and transformation of translators’ prefaces as a literary genre  (when does it emerge, for which texts, what are its genre conventions) and as a praxeological inquiry into the art of translation itself (what know-how has the praxis of itself, how do practitioners’ accounts of their work reflect the well-studied theoretical articulations by such luminaries as Goethe, Schleiermacher, Humboldt, and vice versa?). 

For the source images, see http://www.olmsonline.de/kollektionen/messkataloge .

In its current form, the _Messkataloge_ database contains over 17.3 million individual tokens distributed over the 266 years of its production.

## Sample searches in the Bokeh N-Gram Viewer
 Totals: https://ochre.lib.uchicago.edu/messkataloge/totals.html and https://ochre.lib.uchicago.edu/messkataloge/om_totals.html .

 Cities: https://ochre.lib.uchicago.edu/messkataloge/staedte.html . 

 Genres: https://ochre.lib.uchicago.edu/messkataloge/genres.html . 

 Religions: https://ochre.lib.uchicago.edu/messkataloge/religion.html . 

 Latin: https://ochre.lib.uchicago.edu/messkataloge/apud.html . 
 The preposition “apud” suggests itself here as a proxy for Latinity as it appears in almost all Latin entries and almost none of the German-language entries.


# To install Bokeh for the N-Gram Viewer:

1) make sure you have Python 3.x or Anaconda3 (anaconda.com) installed

2) To check if bokeh is installed -- from the Terminal/command line, do:

   bokeh info

3) If needed, to install bokeh, run:

   pip install bokeh


# To run the Messkataloge Bokeh N-Gram Viewer app:

Unzip all_tokens.zip --> this will create all_tokens.csv

Make sure all_tokens.csv is in the same directory as mk_app.py 

In the Terminal/command line, go to that directory and run:

   bokeh serve --show mk_app.py

The Messkataloge Search & Visualization app will open in a new browser window.

   Use Ctrl-C to exit the app.
