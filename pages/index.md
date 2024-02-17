<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="On Beyond Engineering" %]

-   Research software is software created and run to answer specific questions
-   Usual starting point:
    -   The software is just a piece of laboratory equipment
    -   Papers, theses, and other reports are the product
-   But if the software becomes more popular,
    focus becomes building and sharing software that others can use
-   Your responsibility as a manager is no longer to do things:
    it's to make sure everyone else can do things
    -   The transition is often gradual
-   This tutorial will help
    -   But only if you do the exercises

<!-- ---------------------------------------------------------------- -->
[% section_start class="aside" title="What This Is" %]

-   Notes and working examples that instructors can use to perform a lesson
    -   Do *not* expect novices with no prior Python or Unix experience to be able to learn from them
    -   Musical analogy
        -   This is the chord changes and melody
        -   We expect instructors to create an arrangement and/or improvise while delivering
-   Please see [the license](./license/) for terms of use,
    the [Code of Conduct](./conduct/) for community standards,
    and [these guidelines](./contributing/) for notes on contributing
-   Will cover some technical material, but focus is on teamwork not programming
-   About the author:
    [Greg Wilson][wilson-greg] is a programmer, author, and educator
    -   Co-founder and first Executive Director of [Software Carpentry][carpentries]
    -   Currently a senior software engineering manager at a startup in Toronto

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="Scope" %]

-   [Intended audience][persona]
    -   Ning did a bachelor's degree in economics
        and now works as a data analyst for the Ministry of Health
    -   They learned Python in an intensive 16-week data science bootcamp
        and are comfortable working with Unix command-line tools
        and writing multi-page data analyses
    -   Ning is now in charge of a team
        responsible for building real-time analytics dashboards
        for non-programming staff in the Ministry
    -   They have no prior experience managing a team,
        but had some bad experiences being mismanaged in grad school and internships
-   Prerequisites
    -   Intermediate Unix command line: `find`, `grep`, shell scripts using `for`
    -   Data analysis with Python: Pandas, Plotly, Jupyter notebooks, argparse, regular expressions
    -   Using Git and GitHub on months-long projects with two or three colleagues
-   Learning outcomes
    1.  TODO

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Starting Point" %]

-   Most analyses done in [Jupyter notebooks][jupyter]
    -   Everyone has a [%g sandbox "sandbox" %] Git repository
    -   Analyses and reports (sort of) organized by client and date
-   Some utility code in a shared Git repo
    -   Everyone clones it to their desktop and installs in editable mode
-   Google Docs for reports to [%g stakeholder "stakeholders" %]
    -   Copy/paste figures from notebooks into docs
    -   (Much) easier than the alternatives when collaborating with non-programmers
-   Datasets stored in Google Drive
    -   Everyone downloads what they to the `./data` directory in their sandbox repos
    -   Rely on `.gitignore` to keep this out of version control
-   Ning has to figure out:
    -   What "better" looks like technically [%b Wilson2014 Wilson2017 Irving2021 %]
    -   What it looks like *organizationally*
    -   How to get the team to buy into changes (vs. doing it because they're told to)
    -   How to get the organization to support those changes with more than just words

<!-- ---------------------------------------------------------------- -->
[% section_break class="topic" title="Roles" %]

-   Newcomer's view

<table>
  <thead>
    <tr>
      <th>Role</th>
      <th>Also Called</th>
      <th>What It Does</th>
    </tr>
  </thead>
  <tr>
    <td>Marketing</td>
    <td>Awareness</td>
    <td>Make people aware of who you're trying to help and how</td>
  </tr>
  <tr>
    <td>Sales</td>
    <td>Adoption</td>
    <td>Get people from "this looks interesting" to "we'll pay for it"</td>
  </tr>
  <tr>
    <td>Support</td>
    <td>Success</td>
    <td>Remove roadblocks and providing help</td>
  </tr>
  <tr>
    <td>Human Resources</td>
    <td>Community</td>
    <td>Hiring, firing, promotions, and benefits</td>
  </tr>
  <tr>
    <td>Product Management</td>
    <td></td>
    <td>Translate user pain into requirements</td>
  </tr>
  <tr>
    <td>Project Management</td>
    <td></td>
    <td>Who should work on what right now and how late are we</td>
  </tr>
  <tr>
    <td>Engineering</td>
    <td></td>
    <td>Write, test, debug, and deploy software (hopefully in that order)</td>
  </tr>
</table>

-   A better way to look at it

<table>
  <thead>
    <tr>
      <th>Role</th>
      <th>What Risk It Addresses</th>
    </tr>
  </thead>
  <tr>
    <td>Marketing</td>
    <td>People don't know we exist or how we can help</td>
  </tr>
  <tr>
    <td>Sales</td>
    <td>People won't pay to support our work</td>
  </tr>
  <tr>
    <td>Support</td>
    <td>People struggle to use what we make</td>
  </tr>
  <tr>
    <td>Human Resources</td>
    <td>We don't have the right people and the ones we have aren't happy</td>
  </tr>
  <tr>
    <td>Product Management</td>
    <td>We're building the wrong thing</td>
  </tr>
  <tr>
    <td>Project Management</td>
    <td>People aren't working on the right things or aren't working well together</td>
  </tr>
  <tr>
    <td>Engineering</td>
    <td>We aren't making what we promised we'd make, it doesn't work, or it's not available</td>
  </tr>
</table>

<!-- ---------------------------------------------------------------- -->
[% section_break class="aside" title="In Academia" %]

-   In academia [%b Kuchner2011 %]:
    -   Marketing is publishing papers and giving talks
    -   Sales is getting research grants
-   In open source [%b Eghbal2020 %]:
    -   Marketing is blogging, podcasting, and talking at meetups
    -   Sales is an unsolved problem

<!-- ---------------------------------------------------------------- -->
[% section_break class="exercise" %]

[% exercise %]
Have each person on your team make a list of things they do for your project
every working day,
once a week,
and once each month, quarter, or year.
Label these activities by role.

1.  Who spends most of their time on one kind of thing
    and who is juggling several responsibilities?

2.  Which roles aren't filled by anyone on your team?

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
    -   So people who weren't there know what happened
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

-   Write an [%g elevator_pitch "elevator pitch" %] to help yourself figure out:
    -   Who you're trying to help
    -   What problem they have
    -   What you're doing
    -   Why it's better

> -   Sooner or later, every social scientist has to analyze census data.
> -   A lot of them use CenPlot,
>     but its GUI looks old-fashioned
>     and its scripting interface uses a poorly-documented dialect of Visual Basic.
> -   We're building a new census analysis toolkit called ReCent
>     using [Python][python], [Polars][polars], [Plotly][plotly], and [DVC][dvc].
> -   ReCent will be noticeably faster than CenPlot,
>     particularly on large datasets,
>     and will have a modern web-first interface.
>     It will also offer a comprehensive Python API
>     so that people can integrate it into data analysis pipelines.

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

### Bibliography

[% bibliography %]

### Links

[% link_table %]

[% section_end %]
