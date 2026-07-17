"""Reviewed evidence packs that can be merged into assigned PM workstream tasks.

These presets deliberately contain evidence and source links only. They do not
pre-populate a PM score, recommended score, ceiling, or ranking rationale.
"""

WORKSTREAM_EVIDENCE_PRESETS_VERSION = "v66-evidence-packs-no-rankings-2026-07-17"


def _row(text, links):
    return {"text": text, "links": links}


def _pack(aliases, child_progression, learning_model, development_ecosystem):
    return {
        "aliases": set(aliases),
        "metric_evidence": {
            "child_progression": child_progression,
            "learning_model": learning_model,
            "development_ecosystem": development_ecosystem,
        },
    }


WORKSTREAM_EVIDENCE_PRESETS = {
    "sree_siddaganga_math": _pack(
        [
            "sree siddaganga math", "sri siddaganga math", "siddaganga math",
            "sree siddaganga mutt", "sri siddaganga mutt", "siddaganga mutt",
            "siddaganga matha",
        ],
        _row(
            "The Math has had an Old Boys Association since 1954. Its current association reports about 20,000 life members, but the membership includes both alumni and well-wishers and cannot be treated as 20,000 former students.\nOfficial pages identify Kannada poet Dr. G. S. Shivarudrappa and politician A. S. Patil Nadahalli as alumni.\nNo systematic public evidence was found on Class 10 or 12 completion, college entry, employment, alumni occupations or repeated cohort destinations.\nNo conventional annual or substantive impact report was found; the official publications section contains a monthly magazine and commemorative material rather than outcome reporting.",
            [
                {"label": "Official Math website", "url": "https://siddagangamath.org/siddaganga/home.html"},
                {"label": "Tumakuru district government profile", "url": "https://tumkur.nic.in/en/tourist-place/siddhaganga-mutt/"},
            ],
        ),
        _row(
            "The Gurukula provides primary and basic education, while the associated education society reports a large network spanning high schools, PU colleges, first-grade colleges, ITIs, Sanskrit and Veda schools and specialised institutions.\nThe public material does not explain the Gurukula children's recurring pedagogy, remedial or level-based instruction, assessment mechanisms, mentoring or transition preparation.\nInstitutional scale establishes educational capacity, but does not by itself demonstrate a differentiated learning model for the residential children.\nNo conventional annual or substantive impact report was found; this evidence is based on official website material.",
            [
                {"label": "Official Math website", "url": "https://siddagangamath.org/siddaganga/home.html"},
            ],
        ),
        _row(
            "The official material establishes a long-duration Gurukula serving children from different communities and a separate institutional provision for visually impaired children. Food, shelter and hostel provision are baseline support and are not counted here as Development Environment evidence.\nThe alumni association reports supporting sanitation and campus-development infrastructure through a Gurukula Development Trust.\nNo clear recurring public evidence was found on child-led clubs, organised arts or sport pathways, leadership responsibilities, external mentors, educational travel, public platforms or community projects undertaken by the same child cohort.\nNo conventional annual or substantive impact report was found.",
            [
                {"label": "Official Math website", "url": "https://siddagangamath.org/siddaganga/home.html"},
                {"label": "Tumakuru district government profile", "url": "https://tumkur.nic.in/en/tourist-place/siddhaganga-mutt/"},
            ],
        ),
    ),

    "sri_vishwesha_dhama_gurukulam": _pack(
        [
            "sri vishwesha dhama gurukulam", "sree vishwesha dhama gurukulam",
            "sri vishwesha dhama gurukula", "vishwesha dhama gurukulam",
            "vishwesha dhama gurukula", "svd gurukulam",
        ],
        _row(
            "The official student page gives several named current-student achievements. Aditi and Aneesha Ashok Bhat are reported to have completed multiple external Sanskrit examination levels and won awards; BhuvanaNidhi and Hamsa are reported to have completed Sanskrit or Bhagavad Gita examinations and received external recognitions.\nEeshana is reported to have progressed to another Vidyapeetha and continued advanced study there.\nThese are concrete subject-specific achievements and one educational transition, but the website does not show post-programme alumni destinations such as college, employment or professional arts careers.\nThe full-time residential programme is new, so no residential-cohort outcomes are yet available. No official annual or impact report was located.",
            [
                {"label": "Official student profiles", "url": "https://www.svdgurukulam.org/home/students"},
                {"label": "Official residential programme", "url": "https://www.svdgurukulam.org/programs/full-time-residential"},
            ],
        ),
        _row(
            "Existing evening classes reportedly operate four days each week, with multi-year progression through Sanskrit grammar, classical literature, Vedic texts, external examinations, competitions, recitation and performance.\nThe proposed residential programme combines a detailed six-year classical curriculum with NIOS academics, yoga, games, seva, newspaper reading, lectures, stories and a tightly structured daily schedule.\nThe day-scholar model proposes varying the balance of classical and contemporary subjects according to each child's interests and abilities.\nThe residential model is partly prospective and some curriculum, fee and timetable details were described as awaiting finalisation. No official annual or impact report was located.",
            [
                {"label": "Official programmes", "url": "https://www.svdgurukulam.org/programs"},
                {"label": "Official residential curriculum and schedule", "url": "https://www.svdgurukulam.org/programs/full-time-residential"},
                {"label": "Official subjects page", "url": "https://www.svdgurukulam.org/subjects"},
            ],
        ),
        _row(
            "Student profiles and programme pages show recurring yoga, games, seva, recitation, competitions and cultural performance opportunities beyond ordinary academic instruction.\nThe full residential intake was described as only ten boys aged 9–11 and the campus and residential model were still being established. Meals and accommodation are baseline support and are not counted as Development Environment evidence.\nThe public material does not yet establish sustained child leadership, external mentoring, educational visits, wider community projects or progression through sport and arts for the residential cohort.\nNo official annual or impact report was located.",
            [
                {"label": "Official student profiles", "url": "https://www.svdgurukulam.org/home/students"},
                {"label": "Official residential programme", "url": "https://www.svdgurukulam.org/programs/full-time-residential"},
            ],
        ),
    ),

    "tadimety_radhakrishna_charitable_trust": _pack(
        [
            "tadimety radhakrishna charitable trust", "tadimety radha krishna charitable trust",
            "tadimety radhakrishna trust", "trct",
        ],
        _row(
            "TRCT reports that more than 8,600 economically disadvantaged children and young people have received scholarships and academic enrichment over roughly ten years.\nThis is a reach or assistance figure, not evidence of where recipients subsequently progressed.\nNo named alumni, Class 10 or 12 results, college destinations, course completions, employment outcomes or cohort progression rates were found on the reviewed official pages.\nNo official annual or substantive impact report was located.",
            [
                {"label": "Official TRCT website", "url": "https://www.trct.org/"},
                {"label": "Official scholarship approach", "url": "https://www.trct.org/how-we-do-it"},
            ],
        ),
        _row(
            "The scholarship programme reportedly conducts regular student meetings, monitors academic performance and provides counselling where required.\nThe official pages do not show that TRCT operates a direct school, remedial curriculum, bridge programme, vocational pathway or other substantive teaching model.\nAcademic monitoring and counselling strengthen the scholarship process, but the public evidence does not specify instructional frequency, curriculum, assessment or learning gains.\nNo official annual or substantive impact report was located.",
            [
                {"label": "Official scholarship approach", "url": "https://www.trct.org/how-we-do-it"},
                {"label": "Official projects page", "url": "https://www.trct.org/projects"},
            ],
        ),
        _row(
            "Scholarship recipients may receive counselling, and their families may be involved in economic and family-strengthening programmes. Counselling and financial assistance are not counted by themselves as Development Environment evidence.\nTRCT also reports community initiatives including a public library, drinking-water infrastructure, medicines, school furniture, a proposed government-school auditorium and university research equipment.\nThe public evidence does not show these projects forming one recurring opportunity pathway around the same scholarship children, and no child-led platforms, clubs, arts, sports, mentoring or exposure programme is described.\nNo official annual or substantive impact report was located.",
            [
                {"label": "Official scholarship approach", "url": "https://www.trct.org/how-we-do-it"},
                {"label": "Official projects page", "url": "https://www.trct.org/projects"},
            ],
        ),
    ),

    "sri_ananddhanamma_trust": _pack(
        [
            "sri ananddhanamma charitable trust and seva foundation",
            "sri ananddhanamma charitable trust", "sri ananddhanamma trust",
            "ananddhanamma charitable trust", "ananddhanamma trust",
        ],
        _row(
            "The website mentions scholarships, educational support and assistance for disadvantaged children, but publishes no named students, return-to-school cases, Class 10 or 12 results, college admissions, scholarship destinations, vocational completions or employment outcomes.\nThe organisation's legal objects and stated intentions do not establish achieved child progression.\nNo official annual or impact report was found. The website contains blank sections, placeholder material and broad search-keyword text, which materially limits source reliability.",
            [
                {"label": "Official trust website", "url": "https://sriananddhanammatrust.org/"},
                {"label": "Official activities page", "url": "https://www.sriananddhanammatrust.org/about-us/activities.html"},
            ],
        ),
        _row(
            "The Trust says it promotes free tuition, mentorship, vocational training, scholarships and digital learning, and other pages describe plans to establish schools, academies and colleges.\nThe site does not identify an operating learning centre, current student cohort, teachers, schedule, curriculum, course duration or assessment process.\nProspective language about what the Trust aims or plans to create must not be treated as current educational delivery.\nNo official annual or impact report was found, and the website's placeholder content limits confidence in programme claims.",
            [
                {"label": "Official activities page", "url": "https://www.sriananddhanammatrust.org/about-us/activities.html"},
                {"label": "Official institution plans", "url": "https://www.sriananddhanammatrust.org/about-us/EstablishSchool.html"},
            ],
        ),
        _row(
            "No defined cohort of children is publicly shown receiving recurring arts, sport, clubs, mentoring, leadership roles, public performances, travel or community projects.\nGeneral references to cultural programmes and child welfare are organisational objects, not evidence of an implemented Development Environment.\nDo not describe the Trust as currently operating an orphanage, school, college or disability centre without current programme records.\nNo official annual or impact report was found.",
            [
                {"label": "Official trust website", "url": "https://sriananddhanammatrust.org/"},
                {"label": "Official activities page", "url": "https://www.sriananddhanammatrust.org/about-us/activities.html"},
            ],
        ),
    ),

    "sri_sathya_sai_premaarpitham_foundation": _pack(
        [
            "sri sathya sai premaarpitham foundation", "sri sathya sai premaarpitham",
            "sathya sai premaarpitham foundation", "sai premaarpitham foundation",
        ],
        _row(
            "The official Annual Report 2025 reports a 100% pass rate in the after-school academic programme and says many students ranked between first and fifth in their schools. The programme supports more than 80 regular learners in Grades 1–12.\nThe report does not publish the cohort size behind the pass rate, the examination level, individual marks or year-wise results.\nThe scholarship programme uses home visits, teacher feedback and achievement tracking, but no Class 10 or 12 graduates, college admissions, named scholarship destinations, degree completions or employment outcomes are identified.\nThe 80-page Annual Report 2025 was reviewed; the evidence is current academic performance rather than a documented alumni pathway.",
            [
                {"label": "Official reports page", "url": "https://saipremaarpitham.org/reports/"},
                {"label": "Official education programme", "url": "https://saipremaarpitham.org/education/"},
            ],
        ),
        _row(
            "Vidya Maadhuryam is documented as a daily after-school programme for Grades 1–12 aligned with the Karnataka state syllabus, with personalised teacher attention, weekly and monthly tests, interactive projects, examination preparation, more than 80 regular learners and three teachers.\nThe current website says classes run daily from about 5:30 p.m. to 7:30 p.m.; student accounts describe repeated explanation, internal examinations and unit tests.\nNeed- and merit-based scholarships include family visits and school-level monitoring, supporting continuation but not constituting a teaching method by themselves.\nThe 2025 report described a three-month foundational computer programme as forthcoming, so it is not credited as current delivery.",
            [
                {"label": "Official Annual Report index", "url": "https://saipremaarpitham.org/reports/"},
                {"label": "Official education programme", "url": "https://saipremaarpitham.org/education/"},
            ],
        ),
        _row(
            "Nritya Maadhuryam provides weekly Bharatanatyam instruction through a formal syllabus, with examinations, certifications and community performances; the report says more than 35 children participate across two batches.\nSangeeta Maadhuryam introduces classical vocal music, bhajans and instruments, and students have participated in science exhibitions and stage events.\nThese are recurring cultural and public-presentation opportunities beyond academic tuition. Public evidence is thinner on student leadership, external competitions, career exposure, community projects, travel and sustained external mentorship.\nNutrition, healthcare and the wider ashram setting are not counted here unless they create a demonstrated opportunity pathway for participating children.",
            [
                {"label": "Official Annual Report index", "url": "https://saipremaarpitham.org/reports/"},
                {"label": "Official education programme", "url": "https://saipremaarpitham.org/education/"},
            ],
        ),
    ),

    "sri_durga_foundation": _pack(
        ["sri durga foundation", "sree durga foundation", "durga foundation"],
        _row(
            "The Foundation reports that nearly 1,500 school and college students have received soft-skills training. This measures participation, not education or employment progression.\nNo school-completion, college-admission, job-placement, entrepreneurship, named former-participant or before-and-after destination evidence was found.\nThe phrases 'campus to corporate' and 'job interview preparation' describe programme content, not achieved employment.\nThe Impact page refers to annual reports and case studies, but no accessible substantive report or completed case study was available; impact counters also rendered without usable numbers.",
            [
                {"label": "Official Sri Durga Foundation website", "url": "https://sridurgafoundation.org/"},
                {"label": "Official SDF Paatashala updates", "url": "https://sridurgafoundation.org/category/sdf-paatashala/"},
            ],
        ),
        _row(
            "SDF Paatashala reportedly delivers recurring workshops in government and village schools and colleges covering communication, teamwork, emotional intelligence, problem-solving, public speaking, resume and interview preparation, entrepreneurship, life coaching and self-defence.\nThe Foundation says it designs a curriculum and uses participant feedback to adjust sessions, suggesting more than a one-off workshop.\nThe public material does not specify duration, sessions per student, age-wise curriculum, trainer qualifications, assessment tools, repeat attendance or demonstrated skill gains, and does not clearly separate schoolchildren from college students.\nNo accessible annual or impact report was found.",
            [
                {"label": "Official programme updates", "url": "https://sridurgafoundation.org/category/sdf-paatashala/"},
                {"label": "Official foundation website", "url": "https://sridurgafoundation.org/"},
            ],
        ),
        _row(
            "Public speaking, self-defence and entrepreneurship sessions are part of the Learning Model and are not counted again merely because they are outside the normal school syllabus.\nNo specific evidence was found of the same children receiving recurring external competitions, child-led organisations, public exhibitions or performances, long-term mentors, workplace visits, community projects, leadership responsibilities or travel.\nMeal-distribution beneficiaries under Amritahara cannot be assumed to be the same cohort as SDF Paatashala participants. Food distribution is not Development Environment evidence.\nNo accessible annual or impact report was found.",
            [
                {"label": "Official foundation website", "url": "https://sridurgafoundation.org/"},
                {"label": "Official programme updates", "url": "https://sridurgafoundation.org/category/sdf-paatashala/"},
            ],
        ),
    ),

    "ten_academy_hub_foundation": _pack(
        [
            "ten academy", "hub foundation charitable trust", "hub foundation trust",
            "ten academy hub foundation charitable trust", "ten academy hub foundation",
        ],
        _row(
            "Hub Foundation says Ten Academy began in the 2024–25 academic year and serves more than 50 orphaned or economically disadvantaged children. A June 2025 official article described about 50 children from nursery through Grade 1.\nBecause the school is new and the publicly documented cohort was at early-primary level, no alumni or long-term progression evidence is available.\nNo grade-promotion, retention, school-readiness, transfer, examination or long-term attendance data was found. Parent testimonials about enjoyment or supportive teachers are feedback, not progression outcomes.\nNo official annual or impact report was located.",
            [
                {"label": "Official Hub Foundation website", "url": "https://hubfoundationtrust.org/"},
            ],
        ),
        _row(
            "The official website uses descriptions such as free high-quality education, qualified teachers, structured learning, values, life skills and learning support.\nIt does not explain the curriculum or board, school recognition, daily timetable, teaching methodology, teacher-student ratio, assessment, remedial support, early-childhood goals or language of instruction.\nFuture expansion into higher grades, PUC and degree education is a plan and must not be treated as current delivery.\nNo official annual or impact report was located.",
            [
                {"label": "Official Hub Foundation website", "url": "https://hubfoundationtrust.org/"},
            ],
        ),
        _row(
            "No specific public evidence was found of regular sport, arts, clubs, outdoor learning, child-led projects, public events, mentoring or educational visits.\nA safe and nurturing setting is important but is not, by itself, a demonstrated Development Environment.\nThe official project material has contained conflicting descriptions of whether meals are operating or 'coming soon'; meal provision must be verified and is not counted here as a wider developmental opportunity.\nNo official annual or impact report was located.",
            [
                {"label": "Official Hub Foundation website", "url": "https://hubfoundationtrust.org/"},
            ],
        ),
    ),

    "don_bosco_child_labour_mission_davangere": _pack(
        [
            "don bosco child labour mission", "don bosco child labour mission davangere",
            "dbclm", "dbclm davangere", "don bosco davangere",
        ],
        _row(
            "A silver-jubilee account says former children now occupy 'higher positions' and that past pupils returned for the celebration, but gives no names, education levels, employers, jobs or destination counts.\nA separate province-wide report says 48 students across multiple Don Bosco Young at Risk centres passed the 2022 SSLC examination; that combined figure cannot be assigned specifically to the Davangere mission.\nNo reliable DBCLM-specific evidence was found for Class 10 or 12 completion, college or ITI entry, employment, family reintegration or named former child labourers.\nNo current annual or substantive impact report was located. Evidence from BOSCO Bengaluru must not be attributed to DBCLM Davangere.",
            [
                {"label": "Salesian Province of Bangalore", "url": "https://dbbangalore.org/don-bosco-davangere/"},
            ],
        ),
        _row(
            "The documented historical pathway included non-formal education for dropouts, special education for children withdrawn from labour, reorientation and rehabilitation, school reintegration and community outreach through Suprabha and Sujyothi centres.\nThis is potentially a bridge-and-reintegration model, but the available official material does not explain the current curriculum, assessment, school linkages, daily timetable, age groups, vocational preparation, transition process or current student numbers.\nThe DBCLM website was unavailable during the evidence review, so current implementation remains unverified.\nNo current annual or substantive impact report was located.",
            [
                {"label": "Salesian Province of Bangalore", "url": "https://dbbangalore.org/don-bosco-davangere/"},
            ],
        ),
        _row(
            "DBCLM hosted a youth-leadership programme for nearly 60 youth leaders and ten animators, covering leadership roles, democratic election of state youth leaders and networking across centres. Past pupils have participated in cultural celebrations, and the organisation has hosted child-rights campaigns and camps.\nThese are valuable signals of leadership and civic participation, but public evidence does not establish whether children in the current rehabilitation centres participate regularly; some participants may belong to the broader Don Bosco Youth Movement.\nResidence, rehabilitation care and meals are not counted as Development Environment evidence.\nNo current annual or substantive impact report was located.",
            [
                {"label": "Salesian Province of Bangalore", "url": "https://dbbangalore.org/don-bosco-davangere/"},
            ],
        ),
    ),

    "vikasam_seva_foundation": _pack(
        ["vikasam seva foundation", "vikasam foundation", "vikasam"],
        _row(
            "Vikasam says all children currently enrolled have been integrated into regular schools or Anganwadis. Entry into mainstream settings is meaningful progression, but the website does not state the exact number represented by 'all', the year of integration or whether children remained and progressed there.\nA parent story describes improved daily coping and independence after six months of intervention; this is current functional progress rather than an alumni destination.\nNo public evidence was found on mainstream retention, grade-level learning, school completion, vocational or employment destinations, or outcomes after leaving intervention.\nNo official annual or impact report was located.",
            [
                {"label": "Official Vikasam website", "url": "https://vikasam.com/"},
            ],
        ),
        _row(
            "Vikasam documents a coherent early-intervention pathway: train Anganwadi workers and teachers to identify developmental delays; refer children for assessment; prepare Individualised Education Plans; provide speech, behaviour and occupational interventions; conduct periodic assessments; support integration into Anganwadis and schools; and visit schools to train teachers.\nTherapy is included here because it is tied to communication, functional milestones, school participation and individual learning plans.\nMissing public detail includes assessment instruments, intervention frequency and duration, child-professional ratio, baseline-to-follow-up results, IEP achievement rates, discharge criteria and school-retention data.\nNo official annual or impact report was located.",
            [
                {"label": "Official Vikasam website", "url": "https://vikasam.com/"},
            ],
        ),
        _row(
            "Mainstream inclusion expands children's access to peers and community settings, but it is primarily an outcome of the intervention rather than proof of a separate rich Development Environment.\nNo specific recurring evidence was found of inclusive sport or arts, child-led community participation, performances, competitions, external mentors, clubs, trips, camps or child-choice opportunities.\nAwareness events, parent counselling, transport and therapy are not counted here as child developmental opportunities.\nNo official annual or impact report was located.",
            [
                {"label": "Official Vikasam website", "url": "https://vikasam.com/"},
            ],
        ),
    ),

    "vision_life_foundation": _pack(
        ["vision life foundation", "valley of light foundation"],
        _row(
            "The website says the organisation supports orphaned and underprivileged children through residential education, but publishes no named former residents, Class 10 results, PUC or college admissions, school completions, employment or independent-living destinations.\nTestimonials refer generally to education support and improved circumstances without verifiable progression details.\nNo public annual report, beneficiary count, legal-registration detail, staff list or centre-level outcome data was found. The website alternates between the names Vision Life Foundation and Valley of Light Foundation, which requires identity verification.",
            [
                {"label": "Official Vision Life Foundation website", "url": "https://visionlifefoundation.org/"},
            ],
        ),
        _row(
            "The website states that children in Classes 1–10 receive schooling, moral education, skill-based learning, guidance, counselling and mentorship.\nIt does not identify the schools attended, number or ages of children, study timetable, tutors or teachers, curriculum, remedial instruction, assessments, skill-training content or transition preparation.\nThe phrase 'skill-based learning' is too generic to establish a substantive learning model.\nNo public annual or impact report was found, and current operating scale remains unsubstantiated.",
            [
                {"label": "Official Vision Life Foundation website", "url": "https://visionlifefoundation.org/"},
            ],
        ),
        _row(
            "The website mentions cultural events, games, creative workshops, celebrations and volunteer engagement.\nThese could form useful opportunities if recurring, but no dates, frequency, participant counts, external platforms or evidence of sustained progression are published. Birthday and festival celebrations alone are not sufficient Development Environment evidence.\nResidence, food, shelter, counselling and healthcare are baseline supports and are not counted here.\nNo public annual or impact report was found; the existence, location and current scale of the residential home require direct verification.",
            [
                {"label": "Official Vision Life Foundation website", "url": "https://visionlifefoundation.org/"},
            ],
        ),
    ),

    "vivekananda_girijana_kalyana_kendra": _pack(
        [
            "vivekananda girijana kalyana kendra", "vivekananda girijana kalyana kendra vgkk",
            "vgkk", "v g k k",
        ],
        _row(
            "The official PUC/ITI page reports that 11 ITI students took an all-India career examination in January 2022 and five passed; it also reports that four of the 15 students admitted in 2020–21 dropped out.\nThis is useful completion and attrition evidence, but no job placements after ITI, PUC results, Class 10 results, college destinations, named alumni or school-graduate employment outcomes were found.\nLivelihood activity for broader tribal youth and adults cannot automatically be treated as outcomes of children from the residential school.\nNo current annual report was located; the Resources page was under construction and several figures are visibly from 2021–22.",
            [
                {"label": "Official VGKK website", "url": "https://vgkk.in/"},
            ],
        ),
        _row(
            "The school is described as Kannada-medium, co-educational and following the Karnataka state syllabus, with teachers living on campus. VGKK states that education should be appropriate to tribal language, culture and environment.\nChildren reportedly help maintain the kitchen garden and biogas system and take responsibility for serving food; the campus also includes a science park and laboratory. These may support practical learning and self-reliance.\nThe public pages do not explain how cultural adaptation appears in curriculum, pedagogy, assessment or materials, whether practical responsibilities are curriculum-linked, or how schoolchildren transition into PUC and ITI.\nNo current annual report was located, and activity and enrolment figures require current verification.",
            [
                {"label": "Official VGKK website", "url": "https://vgkk.in/"},
            ],
        ),
        _row(
            "Students reportedly hold real campus responsibilities through the garden, biogas system and meal service rather than only receiving services.\nA five-acre playground supports cricket, basketball, volleyball, kho-kho and kabaddi; a gymnastics room and science park offer additional opportunities. The wider institution is embedded in tribal culture, biodiversity, community rights and livelihoods.\nThe public evidence does not show current competition results, arts or cultural progression, student governance, child-led community research, external mentors or educational tours, and it is unclear which activities remain active in 2026.\nFood, accommodation and healthcare are not counted here as Development Environment evidence.",
            [
                {"label": "Official VGKK website", "url": "https://vgkk.in/"},
            ],
        ),
    ),

    "vonisha_service_foundation": _pack(
        ["vonisha service foundation", "vonisha foundation", "vonisha"],
        _row(
            "Vonisha's Back2School page reports that more than 400 children entered private schools and more than 150 entered government schools between 2017 and 2025. Return to formal education is a valid progression outcome.\nThe website does not report how many remained enrolled, progressed by grade, maintained attendance, completed Class 10 or NIOS, or later dropped out.\nA remedial-programme graduation ceremony shows internal completion but gives no graduate count or subsequent destination. TakeOff reports more than ten young people supported and more than 100 life-skills sessions, but not how many completed Classes 11–12.\nNo downloadable annual report was located; a report was presented at the 2024 annual day but is not publicly available.",
            [
                {"label": "Official Vonisha website", "url": "https://www.vonishafoundation.org/"},
            ],
        ),
        _row(
            "Vonisha publishes a defined education continuum. BridgeEd provides a one-year NIOS Open Basic Education pathway for out-of-school children aged 7–14; Back2School moves learners into government schools, low-cost private schools or NIOS; AfterSchool reinforces formal-school learning; School Finishing supports Grade 8–10 dropouts; and TakeOff adds scholarships, counselling, career planning, spoken English, life skills and mentoring for students aged 14 and above.\nMissing public evidence includes entry assessments, level grouping, class frequency, NIOS results, reintegration-retention rates, stage-completion numbers, teacher ratios and measured learning gains.\nThe website says Vonisha fully managed St. Ignatius Public School only until March 2026, so current operation must not be assumed.\nNo downloadable annual report was located.",
            [
                {"label": "Official Vonisha website", "url": "https://www.vonishafoundation.org/"},
            ],
        ),
        _row(
            "Children have participated in an educational visit to Bannerghatta Biological Park, annual-day dramas, dances and skits, interactions with visiting professionals and senior guests, and life-skills and career-awareness sessions.\nThese provide some exposure and public expression, but the documented field trip is old and annual-day activities are occasional.\nNo strong public evidence was found of regular student leadership, child-led clubs, sustained sport or arts progression, external competitions, long-term professional mentors, community projects, alumni networks or continuing workplace exposure.\nHealth, scholarships and school placement are not counted here as Development Environment evidence.",
            [
                {"label": "Official Vonisha website", "url": "https://www.vonishafoundation.org/"},
            ],
        ),
    ),

    "aban_education_society": _pack(
        [
            "aban education society", "the prime academy", "prime academy aban education society",
            "aban education society the prime academy",
        ],
        _row(
            "The Prime Academy website publishes named educational destinations through student testimonials: Raheen Athani reportedly completed Emergency Medicine and began an internship at KLE Hospital; Owais Tenginkeri completed Radiography and began an internship there; Mahek Makandar and Muhammed Zaheer entered BHMS; and Sana Kamalapur reports BHMS admission after science and entrance preparation.\nThese are specific post-school education and internship destinations, but the website does not state programme dates, the exact intervention received, the total graduating cohort or a denominator.\nThe reported 500+ young people 'guided' cannot be interpreted as 500 successful outcomes.\nNo official annual or impact report was located.",
            [
                {"label": "Official Prime Academy website", "url": "https://theprimeacademy.in/"},
                {"label": "Supplied official terms page", "url": "https://theprimeacademy.in/terms-of-use"},
            ],
        ),
        _row(
            "The website describes free SSLC, PUC and NEET coaching for deserving students; personalised tuition from Class 1 through SSLC; regular testing and examination preparation; small batches; one-to-one mentoring; career counselling; spoken English; personality development; computer basics; and play-based early-childhood education.\nThis establishes an academic coaching and transition-preparation model, particularly around SSLC/PUC and professional-course entry.\nMissing public detail includes timetable, class frequency, free versus paid enrolment, baseline assessment, remedial grouping, annual board and entrance results, teacher qualifications, retention, course completion and selection criteria for 'deserving' students.\nNo official annual or impact report was located.",
            [
                {"label": "Official Prime Academy website", "url": "https://theprimeacademy.in/"},
            ],
        ),
        _row(
            "The current website gives little evidence of a recurring Development Environment beyond the academic pathway. Career counselling and adult mentoring primarily support the Learning Model.\nNursery cultural days, crafts and an indoor play area are part of the core early-childhood offer rather than a wider opportunity system.\nNo specific recurring evidence was found of student-led clubs or governance, sustained sport or arts progression, external competitions or performances, educational visits, community projects, workplace visits or alumni mentoring.\nDo not describe every Prime Group programme as free; the website specifically identifies free coaching for some deserving and underprivileged students.",
            [
                {"label": "Official Prime Academy website", "url": "https://theprimeacademy.in/"},
            ],
        ),
    ),

    "aikya_trust": _pack(
        ["aikya trust", "aikya", "aikya trust ghps old anekal"],
        _row(
            "For the 2024–25 academic year, Aikya reports that three supported students qualified for the Karnataka National Means-cum-Merit Scholarship examination. This is a concrete external scholarship-selection outcome.\nNo public evidence was found on Class 10 completion, PUC or college destinations, repeated scholarship cohorts, employment, named former students or long-term retention following primary-school support.\nKnowledge exhibitions, science fairs and school participation are current learning activities rather than alumni outcomes.\nNo annual or impact report was located; the evidence is based on detailed official school and activity pages.",
            [
                {"label": "Official GHPS Old Anekal page", "url": "https://www.aikyatrust.org/ghps-old-anekal"},
                {"label": "Official Aikya website", "url": "https://www.aikyatrust.org/"},
            ],
        ),
        _row(
            "Aikya's foundational-learning model includes activity-based teaching for Classes 1–3, foundational literacy and numeracy rooms, phonics and numeracy training for teachers, hands-on mathematics materials, science laboratories, supplemental teachers, remedial summer camps, experiential science and mathematics, parent orientation and parent-teacher engagement.\nAt GHPS Old Anekal, it introduced LKG–UKG, recruited teachers and supplied books, learning materials and academic guidance.\nMissing evidence includes baseline and endline results, child-level progression, consistency across schools, teacher attendance and observation systems, class frequency, current enrolment by school and outcomes of remediation.\nNo annual or impact report was located.",
            [
                {"label": "Official GHPS Old Anekal page", "url": "https://www.aikyatrust.org/ghps-old-anekal"},
                {"label": "Official Aikya website", "url": "https://www.aikyatrust.org/"},
            ],
        ),
        _row(
            "Aikya documents a Knowledge Expo where about 350 students from two schools presented projects to families, nearby schools and visitors; sponsorship and training for a girls' kabaddi team; long-jump practice infrastructure; a 23-day summer camp involving more than 110 children; seed-ball and kitchen-garden work; and a community planting initiative involving students, parents, teachers and former students.\nThese are meaningful public-presentation, sport and environmental responsibility opportunities beyond ordinary instruction.\nThe activities occurred across different schools and academic years, so they must not be attributed to every Aikya-supported child.\nNo annual or impact report was located.",
            [
                {"label": "Official Aikya website", "url": "https://www.aikyatrust.org/"},
                {"label": "Official GHPS Old Anekal page", "url": "https://www.aikyatrust.org/ghps-old-anekal"},
            ],
        ),
    ),

    "ananda_suvarna_rural_development_trust": _pack(
        [
            "ananda suvarna rural development trust", "ananda suvarna trust",
            "ananda suvarna master unit", "ananda suvarna",
        ],
        _row(
            "The official Ananda Marga project page says the school has operated for more than a decade with 250+ students and provides free education, materials, higher-study support and transport.\nNo Class 10 or 12 results, numbers progressing to higher study, colleges, courses, scholarships, named former students or employment outcomes were published.\nThe phrase 'higher study support' establishes an input, not an achieved destination, and the 250+ figure measures institutional scale rather than alumni progression.\nNo annual or school impact report was found.",
            [
                {"label": "Official Ananda Suvarna project page", "url": "https://india.anandamarga.org/projects/ananda-su"},
            ],
        ),
        _row(
            "The public page establishes a continuing school but gives little information on how learning occurs.\nIt does not specify grades, board affiliation, language of instruction, teaching approach, remedial or bridge education, assessment, teacher numbers, class frequency, vocational pathways or transition preparation.\nFree schooling, buildings, materials and transport are access provisions rather than a differentiated Learning Model.\nNo annual or school impact report was found.",
            [
                {"label": "Official Ananda Suvarna project page", "url": "https://india.anandamarga.org/projects/ananda-su"},
            ],
        ),
        _row(
            "A playground and broad cultural or social-development objectives are mentioned, but no actual recurring child opportunities are described.\nNo specific evidence was found of organised sport, arts or public performance, clubs, competitions, student responsibility, child-led community projects, educational visits, mentors or alumni networks.\nHealth camps, school transport and basic support are not counted as Development Environment evidence.\nNo annual or school impact report was found.",
            [
                {"label": "Official Ananda Suvarna project page", "url": "https://india.anandamarga.org/projects/ananda-su"},
            ],
        ),
    ),

    "belakoo_trust": _pack(
        ["belakoo", "belakoo trust", "belakoo foundation"],
        _row(
            "Belakoo reports that the last three Class 10 batches at its Hangrapura campus all passed in first class, with one student scoring 94.6%; cohort sizes, years and later destinations are not stated.\nFor a CET Bootcamp serving about 150 girls, it reports 24 engineering-college admissions with scholarships, more than 20% ranking within the first 50,000 and a 67% year-on-year performance increase. The underlying baseline for the percentage increase is not published.\nA named story describes Madhukumar progressing from digital-equipment and counselling support to a diploma and then placement at an institute associated with Maruti Udyog.\nThese results come from different programmes and must not be merged into one cohort-success rate. Listed annual and impact reports were inaccessible during review.",
            [
                {"label": "Official Belakoo website", "url": "https://www.belakoo.in/"},
            ],
        ),
        _row(
            "Belakoo's Hangrapura programme uses an in-house Belakube approach focused on STEAM fundamentals and learning by doing; the site says more than 170 children completed over 70 classes.\nThe CET programme is documented as 180 hours of coaching over 30 days, with experienced teachers, printed study materials, practice papers, two mock examinations per subject and counselling on rank, seat and college selection.\nMissing evidence includes current frequency across all campuses, baseline assessment, learner grouping, teacher-child ratios, repeated CET results, NEET results and full Class 10 cohort numbers.\nAnnual and impact reports are listed on the site, but the linked files were inaccessible during review.",
            [
                {"label": "Official Belakoo website", "url": "https://www.belakoo.in/"},
            ],
        ),
        _row(
            "Belakoo's Celebrating Our Differences initiative provides public performances for children from NGOs, government schools and special schools; one edition reportedly involved more than 100 children with special needs.\nAn art exhibition gives children a public platform, Learning Expeditions take children outside their immediate setting, and volunteer teachers expose children to adults from varied professions.\nThese are credible public-visibility and exposure opportunities, but performers and participants are drawn from several organisations and may not be the same children attending Belakoo's regular campuses.\nAnnual and impact reports are listed on the site, but the linked files were inaccessible during review.",
            [
                {"label": "Official Belakoo website", "url": "https://www.belakoo.in/"},
            ],
        ),
    ),

    "cherysh_trust": _pack(
        ["cherysh trust", "cherysh", "cherysh foundation", "cherysh trust tata backed"],
        _row(
            "The FY 2025–26 annual report does not publish school-completion, college or employment destinations for children.\nIt notes that some current Learning Facilitators were formerly students in CherYsh classrooms and now work as village educators. This is a potentially important education-to-employment pathway, but no count, names or years are provided.\nBaseline-to-endline learning gains, Spell Bee participation, coding projects and current enrolment are current programme evidence rather than alumni outcomes.\nThe 24-page Annual Report FY 2025–26 was opened and reviewed.",
            [
                {"label": "Official annual reports", "url": "https://cherysh.org/financial-reports/"},
                {"label": "Official CherYsh overview", "url": "https://cherysh.org/about-us/"},
            ],
        ),
        _row(
            "The FY 2025–26 report gives total programme reach of 3,367 children across 94 villages, while not clearly establishing whether every child is unique across programmes.\nJunior Shiksha uses structured Mathematics, English and phonics materials, Level 1–4 progression, locally recruited Learning Facilitators and monthly facilitator training. The report publishes baseline-to-endline gains across English and Mathematics for Classes 1–4.\nEnglish Shiksha uses a phonics-first curriculum; E-Shiksha includes Scratch, LibreOffice and practical digital projects.\nThe report says only three E-Shiksha centres were active while 16 Haliyal centres were suspended; this current-delivery limitation must be retained.",
            [
                {"label": "Official annual reports", "url": "https://cherysh.org/financial-reports/"},
                {"label": "Official CherYsh Educate programme", "url": "https://cherysh.org/about-us/"},
            ],
        ),
        _row(
            "CherYsh reports a programme-wide Spell Bee, E-Shiksha exhibitions where children demonstrated technical projects, interaction with engineering students from KLE Tech University, and arts, games, songs, plays and sports across Shiksha centres.\nThese create public-presentation opportunities and exposure to external university students.\nPublic evidence is weaker on child-led governance, sustained external mentoring by child, repeated science or arts competitions, educational travel, leadership roles and long-term progression through specific interests.\nThe FY 2025–26 annual report was reviewed; activities across different centres must not be attributed to every child.",
            [
                {"label": "Official annual reports", "url": "https://cherysh.org/financial-reports/"},
                {"label": "Official CherYsh overview", "url": "https://cherysh.org/about-us/"},
            ],
        ),
    ),

    "chethana_special_school": _pack(
        ["chethana special school", "chetana special school", "chethana school"],
        _row(
            "The official achievements page reports that five students transitioned into regular schools, four passed SSLC and eleven former students are working and earning livelihoods.\nA separate 2023–24 update names Dwithi Chandra and Priyanka as SSLC passers; they may already be included in the cumulative figure of four and must not be added without confirmation.\nThe website does not identify employers, job roles, earnings, placement year or retention for the eleven working former students, or the schools entered by the five mainstreamed students.\nNo annual report was located. The About page also contains conflicting current-enrolment figures of 90 and 110 students.",
            [
                {"label": "Official Chethana website", "url": "http://www.chethanaspecialschool.com/aboutus.html"},
            ],
        ),
        _row(
            "Chethana reports using the Madras Developmental Programming System and BASIC-MR behavioural assessment scales, with an academic pathway that allows appropriate learners to sit SSLC after age 15.\nIts model includes literacy, computers, tailoring, vocational training, personal-hygiene training, speech services and physiotherapy. Therapy is included here where it supports communication, functioning and learning.\nMissing public detail includes Individual Education Plans, assessment frequency, functional groupings, numbers in academic versus vocational pathways, the SSLC preparation process, vocational trades and certification, and placement preparation.\nNo annual report was located.",
            [
                {"label": "Official Chethana website", "url": "http://www.chethanaspecialschool.com/aboutus.html"},
            ],
        ),
        _row(
            "The official achievements record includes national-level para-sport medals and international-athletics selection, national bocce and cycling results, state-level folk dance and sport, national online dance, painting, yoga and singing competitions, Quizabled, district cultural competitions, Yakshagana, and exhibitions and sales of products made by students.\nOne institution reportedly purchased 1,000 student-made diyas, creating contact with real customers. These are substantive competitive, public-recognition and market-facing opportunities.\nMany achievements span 2005–23 and demonstrate institutional history rather than proving that every pathway remains active in 2026.\nNo annual report was located.",
            [
                {"label": "Official Chethana website", "url": "http://www.chethanaspecialschool.com/aboutus.html"},
            ],
        ),
    ),

    "eka_educational_charitable_trust": _pack(
        [
            "eka educational and charitable trust", "eka educational charitable trust",
            "eka inclusion", "eka trust",
        ],
        _row(
            "Eka states that its work develops employability and creates job opportunities, but no named former students placed, employer or role, NIOS Class 10 or 12 result, course completion, earnings, placement rate or independent-living destination was found.\nThe weekend programme also serves people who are already employed or between jobs; pre-existing employment cannot be counted as an outcome created by Eka.\nThe homepage claims 120 students impacted and 50 workshops without a reporting year, beneficiary definition or deduplication method.\nOnly 2019–20 and 2020–21 Annual Day slide decks are listed; no current substantive annual or impact report was found.",
            [
                {"label": "Official Eka Inclusion website", "url": "https://ekainclusion.com/"},
            ],
        ),
        _row(
            "Eka publishes a disability-specific model including individualised learning plans, evidence-based teaching, an average class ratio of about 1:4, trained special educators and psychologists, multisensory instruction, assistive technology, functional academics, remedial support across several school boards, critical thinking, transition planning, three-month culinary courses, and relationships, consent and sex education for young adults.\nThis is a detailed model on paper. The central evidence gap is implementation and progression: no assessment results, board results, learner movement, course-completion numbers, placement conversion or current enrolment by pathway is published.\nOnly old Annual Day slide decks are available; no current substantive annual or impact report was found.",
            [
                {"label": "Official Eka Inclusion website", "url": "https://ekainclusion.com/"},
            ],
        ),
        _row(
            "Potential wider opportunities include a Youth Ambassadors Project for mainstream high-school and PUC students, inclusion-awareness work and an e-commerce initiative intended to expose teenagers and young adults with disabilities to entrepreneurship.\nThe project page describes these initiatives as being under development and does not publish participant counts, frequency, completed outputs, public roles or income results. They must therefore be treated as programme intentions rather than proven Development Environment pathways.\nTherapy, counselling and supportive relationships are not counted here by themselves.\nNo current substantive annual or impact report was found.",
            [
                {"label": "Official Eka Inclusion website", "url": "https://ekainclusion.com/"},
            ],
        ),
    ),

    "helping_hands_together": _pack(
        ["helping hands together", "helping hands together trust", "helping hands together foundation"],
        _row(
            "No named beneficiary, school result, school-reintegration case, college or training destination, employment outcome or former-resident pathway was found.\nThe website is predominantly broad trust objectives and governance provisions, not evidence of achieved child progression.\nNo annual report, activity report or substantive programme document was located. Repeated unexplained 88% figures, template filler text and prospective wording materially limit source reliability.",
            [
                {"label": "Official Helping Hands Together website", "url": "https://helpinghandstogether.org.in/"},
            ],
        ),
        _row(
            "The website refers to literacy, skill development and formal or non-formal educational institutions, but these appear as legal objects or future intentions.\nNo operating centre, current child cohort, teacher, curriculum, timetable, assessment, class frequency, course duration or learning outcome is publicly demonstrated.\nThe site therefore does not establish an implemented Learning Model.\nNo annual report, activity report or substantive programme document was located.",
            [
                {"label": "Official Helping Hands Together website", "url": "https://helpinghandstogether.org.in/"},
            ],
        ),
        _row(
            "No defined child cohort is shown receiving recurring arts, sport, leadership, mentoring, public platforms, educational visits or community projects.\nReferences to cultural events, seminars and environmental campaigns are broad objectives rather than documented child participation.\nDo not infer that the organisation currently runs an orphanage, school, regular child-meal programme or verified 100-volunteer operation from the website copy alone. Food, shelter and healthcare are not counted as Development Environment evidence.\nNo annual report, activity report or substantive programme document was located.",
            [
                {"label": "Official Helping Hands Together website", "url": "https://helpinghandstogether.org.in/"},
            ],
        ),
    ),

    "inchara_foundation": _pack(
        ["inchara foundation", "in chara foundation", "inchara"],
        _row(
            "InChara's official material describes rehabilitation, reintegration, aftercare and support toward sustainable livelihoods for children and young adults affected by sexual abuse.\nThe public pages do not publish named former residents, school-completion results, college destinations, vocational certifications, employment counts or a cohort-based reintegration or livelihood rate.\nReported reintegration and livelihood support should therefore be treated as pathway claims rather than documented alumni outcomes.\nNo official annual or substantive impact report was located during the evidence review.",
            [
                {"label": "Official InChara Foundation website", "url": "https://incharafoundation.org/"},
                {"label": "Official Our Work page", "url": "https://incharafoundation.org/ourwork/"},
            ],
        ),
        _row(
            "The official programme description combines a licensed rehabilitation home with access to education, skill development, psychological support, legal assistance, family work, reintegration and aftercare.\nThis establishes a multi-stage rehabilitation pathway, but the public material does not specify the educational curriculum, tutoring frequency, baseline assessment, individual learning plans, vocational course duration, certifications or transition milestones.\nPsychological support is relevant to the rehabilitation model but is not evidence of academic progression by itself.\nNo official annual or substantive impact report was located during the evidence review.",
            [
                {"label": "Official Our Work page", "url": "https://incharafoundation.org/ourwork/"},
                {"label": "Official InChara Foundation website", "url": "https://incharafoundation.org/"},
            ],
        ),
        _row(
            "The organisation describes creative activities, child-voice and awareness platforms, family and community engagement, legal advocacy and aftercare support. These indicate potential opportunities for expression and agency beyond formal instruction.\nThe public material does not quantify how frequently children participate, which activities are recurring, whether children hold leadership roles, or whether there are sustained arts, sport, mentoring, exposure or community-project pathways.\nSafe shelter, food, healthcare, therapy and legal case support are important baseline and protection services but are not counted here as Development Environment evidence.\nNo official annual or substantive impact report was located.",
            [
                {"label": "Official Our Work page", "url": "https://incharafoundation.org/ourwork/"},
                {"label": "Official InChara Foundation website", "url": "https://incharafoundation.org/"},
            ],
        ),
    ),

    "matoshree_ambubai_residential_school": _pack(
        [
            "matoshree ambubai residential school", "matoshree ambubai residential school for blind girls",
            "ambubai residential school", "ambubai school for blind girls", "matoshree ambubai",
        ],
        _row(
            "The official website provides named success stories, including girls who entered the residential school and continued their education, but does not publish a complete cohort, Class 10 or 12 completion rate, college destinations, employment rate or repeated alumni pathway.\nIndividual stories are useful qualitative evidence but cannot be converted into a programme-wide success rate without the number of girls served and their later destinations.\nThe school's reports page lists annual-report material, but the linked document was not accessible during review; the evidence pack therefore relies on the official website and named stories rather than a fully read report.",
            [
                {"label": "Official school website", "url": "https://ambubaischoolforblindgirls.org/"},
                {"label": "Official success stories", "url": "https://ambubaischoolforblindgirls.org/success-stories/"},
                {"label": "Official reports page", "url": "https://ambubaischoolforblindgirls.org/report/"},
            ],
        ),
        _row(
            "The school describes free education and specialised training for visually impaired girls aged roughly 6–18 within a residential setting.\nThe public material establishes a disability-specific educational institution but gives limited detail on the board or grade structure, Braille and assistive-technology curriculum, individual assessment, remedial instruction, teacher ratios, vocational preparation or transition into higher education and work.\nResidence, food and basic care are access supports rather than a differentiated Learning Model by themselves.\nThe listed annual-report document was not accessible during review.",
            [
                {"label": "Official school website", "url": "https://ambubaischoolforblindgirls.org/"},
                {"label": "Official reports page", "url": "https://ambubaischoolforblindgirls.org/report/"},
            ],
        ),
        _row(
            "The public pages indicate that girls receive opportunities intended to build independence and participate in school activities, but the available evidence is not detailed enough to establish the frequency or progression of arts, sport, clubs, public performance, leadership, mentoring, educational travel or community projects.\nNamed success stories may include confidence and self-reliance, but these should not be treated as a recurring Development Environment for every resident without programme records.\nResidential care, food, mobility support and healthcare are not counted here as wider developmental opportunities.\nThe listed annual-report document was not accessible during review.",
            [
                {"label": "Official school website", "url": "https://ambubaischoolforblindgirls.org/"},
                {"label": "Official success stories", "url": "https://ambubaischoolforblindgirls.org/success-stories/"},
            ],
        ),
    ),

    "prachodana_open_shelter": _pack(
        [
            "prachodana ngo open shelter programme", "prachodana open shelter programme",
            "prachodana ngo", "prachodana", "prachodana open shelter",
        ],
        _row(
            "Prachodana's official site describes an Open Shelter for children in need of care and protection and separately lists a Bridge School, Childline and success-story sections.\nNo public quantified evidence was found on family reunification, formal-school reintegration, Class 10 or 12 completion, vocational completion, employment or named post-programme destinations for the Open Shelter cohort.\nA shelter admission, rescue or participation count is not by itself a child-progression outcome.\nNo current official annual or substantive impact report was located during the evidence review.",
            [
                {"label": "Official Open Shelter programme", "url": "https://www.prachodanahassan.org/programmes/open-shelter/"},
                {"label": "Official Prachodana website", "url": "https://www.prachodanahassan.org/"},
            ],
        ),
        _row(
            "The programme architecture links outreach and child-protection response with an Open Shelter and a Bridge School, suggesting a potential pathway from crisis support toward education and reintegration.\nThe public pages do not specify the current number of children, bridge-school curriculum, class frequency, baseline assessment, age or level grouping, school-transition process, examination results, vocational preparation or current staffing.\nProtection, counselling and shelter are important parts of the intervention but do not demonstrate the instructional model without further detail.\nNo current official annual or substantive impact report was located.",
            [
                {"label": "Official programmes page", "url": "https://www.prachodanahassan.org/programmes/"},
                {"label": "Official Open Shelter programme", "url": "https://www.prachodanahassan.org/programmes/open-shelter/"},
            ],
        ),
        _row(
            "Prachodana's wider site refers to awareness, training, workshops and child-rights work, but it does not show which recurring arts, sport, leadership, mentoring, public-expression, educational-visit or community-project opportunities are received by the Open Shelter children.\nOpen-shelter care, food, protection, healthcare and counselling are baseline services and are not counted here as Development Environment evidence.\nActivities delivered to other Prachodana programmes should not be assigned to the shelter cohort without confirmation.\nNo current official annual or substantive impact report was located.",
            [
                {"label": "Official Prachodana website", "url": "https://www.prachodanahassan.org/"},
                {"label": "Official Open Shelter programme", "url": "https://www.prachodanahassan.org/programmes/open-shelter/"},
            ],
        ),
    ),

    "rebuild_india_foundation": _pack(
        ["rebuild india foundation", "rebuild india", "noble international school rebuild india"],
        _row(
            "Rebuild India publishes narrative impact stories and broad claims that students become graduates, leaders or entrepreneurs, including individual stories on its website.\nThe reviewed public pages do not provide a defined cohort, dates, school-completion figures, board results, college destinations, scholarship conversion, employment outcomes or a repeated alumni pathway that can be checked against programme enrolment.\nIndividual donor-facing stories should be retained as reported stories rather than converted into programme-wide outcome rates.\nNo official annual or substantive impact report was located during the evidence review.",
            [
                {"label": "Official Rebuild India website", "url": "https://www.rebuildindia.org.in/"},
                {"label": "Official impact stories", "url": "https://www.rebuildindia.org.in/home-1-1-1-1-2-1"},
            ],
        ),
        _row(
            "The Noble International School pages describe a balanced academic curriculum with value-based education, leadership and entrepreneurship, hands-on projects, real-world problem-solving and scholarship support.\nThese descriptions suggest a broad school model, but the public material does not clearly establish board recognition, current grades and enrolment, timetable, teacher numbers and qualifications, assessment practice, remedial support, measured learning gains or transition results.\nScholarships are an access input and are not a teaching method by themselves.\nNo official annual or substantive impact report was located.",
            [
                {"label": "Official Noble International School page", "url": "https://www.rebuildindia.org.in/home-1-1-1-1-1-2-1-1-1-1-1-1"},
                {"label": "Official Rebuild India website", "url": "https://www.rebuildindia.org.in/"},
            ],
        ),
        _row(
            "The school pages describe sport and yoga, arts including music, dance and drama, leadership and entrepreneurship projects, and community engagement or service.\nThese are potentially meaningful opportunities beyond core academics, but the public evidence does not state participation numbers, frequency, external platforms, student leadership roles, competition progression, mentor relationships or completed community projects.\nThe website's broad donor-facing language should not be treated as proof that every student receives all listed opportunities.\nNo official annual or substantive impact report was located.",
            [
                {"label": "Official Noble International School page", "url": "https://www.rebuildindia.org.in/home-1-1-1-1-1-2-1-1-1-1-1-1"},
                {"label": "Official Rebuild India website", "url": "https://www.rebuildindia.org.in/"},
            ],
        ),
    ),

    "samarpan_foundation": _pack(
        ["samarpan", "samarpan foundation", "samarpan foundation india"],
        _row(
            "Samarpan's project pages and annual-report archive document education and child-support programmes, including schools or tuition centres and children's homes in different locations.\nThe reviewed public summaries do not provide a consistent cohort of named former students, Class 10 or 12 completion rates, college destinations, vocational certification, employment outcomes or a repeated cradle-to-career pathway attributable to one programme.\nFormal-school enrolment, sponsorship and children reached are inputs or intermediate progression unless retention and completion are also shown.\nAn official Annual Report 2024–25 is publicly listed and was used alongside official project pages; no unsupported destination rate is inferred from it.",
            [
                {"label": "Official Samarpan projects", "url": "https://samarpanfoundation.org/projects"},
                {"label": "Official Samarpan reports and profile", "url": "https://samarpanfoundation.org/about"},
                {"label": "Annual Report 2024–25", "url": "https://samarpan.blr1.cdn.digitaloceanspaces.com/downloads/Annual-Report-2024-25-Low-Res.pdf"},
            ],
        ),
        _row(
            "Samarpan reports operating education initiatives such as a school and tuition centre in Kishangarh, a tuition centre in Chimbel and educational support linked to children's homes.\nThe model includes formal-school access, tuition or learning support, education materials and community-based work. Public material does not consistently specify curriculum, class frequency, baseline assessment, learner grouping, teacher ratios, annual learning results, remediation or transition preparation across each site.\nEvidence from different Samarpan projects must not be merged into one uniform learning model without site-level verification.\nThe official Annual Report 2024–25 and project pages were used for this pack.",
            [
                {"label": "Official Samarpan projects", "url": "https://samarpanfoundation.org/projects"},
                {"label": "Annual Report 2024–25", "url": "https://samarpan.blr1.cdn.digitaloceanspaces.com/downloads/Annual-Report-2024-25-Low-Res.pdf"},
            ],
        ),
        _row(
            "Samarpan's project model is community-based and may include activities for children across schools, tuition centres and homes, but the reviewed public material gives limited site-specific evidence on recurring child-led clubs, sport or arts progression, public performances, external mentors, educational visits, leadership roles or community projects.\nActivities from one location should not be attributed to every Samarpan child or site.\nResidence, food, healthcare, sponsorship and basic protection are not counted here as Development Environment evidence.\nThe official Annual Report 2024–25 and project pages were used for this pack.",
            [
                {"label": "Official Samarpan projects", "url": "https://samarpanfoundation.org/projects"},
                {"label": "Annual Report 2024–25", "url": "https://samarpan.blr1.cdn.digitaloceanspaces.com/downloads/Annual-Report-2024-25-Low-Res.pdf"},
            ],
        ),
    ),
}
