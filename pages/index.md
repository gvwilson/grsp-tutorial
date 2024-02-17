<!-- ---------------------------------------------------------------- -->
[% section_start class="aside" title="What This Is" %]

-   notes and working examples that instructors can use to perform a lesson
    -   do *not* expect novices with no prior Python or Unix experience to be able to learn from them
-   musical analogy
    -   this is the chord changes and melody
    -   we expect instructors to create an arrangement and/or improvise while delivering
    -   see [*Teaching Tech Together*][t3] for background
-   please see [the license](./license/) for terms of use,
    the [Code of Conduct](./conduct/) for community standards,
    and [these guidelines](./contributing/) for notes on contributing
-   about the author:
    [Greg Wilson][wilson-greg] is a programmer, author, and educator based in Toronto

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Scope" %]

-   [intended audience][persona]
    -   Ning did a bachelor's degree in economics
        and now works as a data analyst for the Ministry of Health
    -   They learned Python in an intensive 16-week data science bootcamp program
        and are comfortable working with Unix command-line tools
        and writing data analysis programs with Python
    -   Ning has been put in charge of a new team
        responsible for building analytics dashboards
	that people in the Ministry can use to query data in real time
    -   They have no prior experience managing a team or a long-lived project
-   prerequisites
    -   intermediate Unix command line: `find`, `grep`, shell scripts using `for`
    -   data analysis with Python: Pandas, Plotly, Jupyter notebooks, argparse, regular expressions
    -   using Git and GitHub on months-long projects with two or three colleagues
-   learning outcomes
    1.  TODO

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Meetings" %]

-   People don't hate meetings: they hate badly-run meetings
    -   Which are the only kind most people have seen
-   Does there actually need to be a meeting?
-   Create an agenda
    -   Include timings
    -   Plan to run for 25 or 50 minutes
-   Have clear rules for making decisions
-   Have a moderator
    -   Call on specific people
    -   One point at a time
    -   No interruptions or side conversations
-   Establish meeting protocol
    -   "Are we chatting in Zoom, on Slack, or in the Google Doc?"
    -   "How do I raise my hand?"
-   Take notes
    -   So people who weren’t there know what happened
    -   So people who were there agree what happened
    -   So people can be held accountable at later meetings
    -   "Notes" may take the form of updated tickets
-   Shallow, then deep
    -   First lap: three-sentence rule
    -   Sort issues by priority and discuss in order
    -   Progress, plans, and problems go in
    -   Context and priorities come out

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Read "[Dealing with Disruptive Behaviors](@root/files/noaa-facilitating-disruptive.pdf)"
and decide which of the ten stereotypes you fit.

<table>
  <tr>
    <td>Apathetic Flounder</td>
    <td>Argumentative Jellyfish</td>
    <td>Arrogant Sea Lion</td>
    <td>Blowfish</td>
    <td>Complaining Crab</td>
  </tr>
  <tr>
    <td>Diverting Dolphin</td>
    <td>Dominating Shark</td>
    <td>Eager Sea Otter</td>
    <td>Indecisive Octopus</td>
    <td>Shy Clam</td>
  </tr>
</table>

[% exercise %]
The next time you are in a meeting,
draw a grid and label the rows and columns with the participants' names.
Each time person X interrupts person Y,
add a tick at location XY.
What you will probably see is:

1.  The same few people do most of the interrupting.

2.  They only interrupt people they perceive as having lower social status within the group
    (i.e., they interrupt down but not up).

Be sure to include your own interruptions in your grid.

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Direction" %]

-   Write an [%g elevator_pitch "elevator pitch" %]
    -   Who you're trying to help
    -   What problem they have
    -   What you're doing
    -   Why it's better
-   Example:
    -   Sooner or later, every social scientist has to analyze census data.
    -   A lot of them use CenPlot,
        but its GUI looks old-fashioned
        and its scripting interface uses a poorly-documented dialect of Visual Basic.
    -   We're building a new census analysis toolkit called ReCent
        using [Python][python], [Polars][polars], [Plotly][plotly], and [DVC][dvc].
    -   ReCent will be noticeably faster than CenPlot,
        particularly on large datasets,
        and will have a modern web-first interface.
        It will also offer a comprehensive Python API
        so that people can integrate it into data analysis pipelines.
-   *Don't* make the same unverifiable claims that you mock in others' pitches
    -   E.g., "a flexible, intuitive interface":
        have you ever seen anyone describe their system as inflexible and confusing?
-   Internal: ensure everyone on the team understands what the goal is
    -   Enables team members to make small decisions independently and consistently
-   External: allows busy people to decide if they care or not
    -   Most people won't
    -   But they'll thank you for helping them figure that out quickly
-   Review and update your pitch at least once a year

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Write an elevator pitch for a tool you use regularly,
then compare your pitch with what you see on the tool's home page
*without scrolling down*.
How well is the tool explaining its purpose and benefits?

[% exercise %]
Have each member of your team write an elevator pitch for your project
simultaneously and independently,
then compare those pitches.
Where is there agreement?
Where are there gaps?
Where do people disagree on who they're trying to help and how?

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Appendices" %]

### Terms

[% glossary %]

### Acknowledgments

This tutorial would not exist without the help of:

[% thanks %]

### Links

[% link_table %]

[% section_end %]
