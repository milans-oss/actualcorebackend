"""Reviewed evidence packs that can be merged into assigned PM workstream tasks.

These presets deliberately contain evidence and source links only. They do not
pre-populate a PM score, recommended score, ceiling, or ranking rationale.
"""

WORKSTREAM_EVIDENCE_PRESETS_VERSION = "v69-piyush-10-to-24-evidence-packs-2026-07-17"


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

    "agastya_international_foundation": _pack(
        [
            "agastya international foundation", "agastya foundation", "agastya",
        ],
        _row(
            "Agastya's 2023–24 Annual Report documents participant progression within its science and leadership programmes rather than a conventional school-completion pathway. Young Instructor Leader participants received scholarships totalling ₹625,000, and the report says about 7% of YIL participants entered national or international STEM competitions and won awards. The organisation also maintains qualitative 'Transformed Lives' stories and piloted career guidance for YIL participants.\nThe public material does not provide a cohort table linking Agastya participation to Class 10 or 12 completion, college admission, degree completion or employment. Competition participation, scholarships and individual stories should therefore be presented as intermediate progression signals, not a programme-wide alumni destination rate.\nThe official 2023–24 Annual Report was located and reviewed alongside the official programme and impact pages.",
            [
                {"label": "Official Annual Report 2023–24", "url": "https://www.agastya.org/_files/ugd/eee33c_92a5aeebcbc84ce48d9aef9ac5247acc.pdf"},
                {"label": "Official publications page", "url": "https://www.agastya.org/publications"},
                {"label": "Official impact page", "url": "https://www.agastya.org/impact"},
            ],
        ),
        _row(
            "Agastya's learning model is built around hands-on, inquiry-led science and mathematics for underserved government-school children. Mobile Science Labs carry more than 100 working models to remote schools and typically deliver two- to three-hour experimental sessions for Grades 5–10. Science Centres provide repeated project-based and discovery-based learning, camps and fairs, while the Campus Creativity Lab integrates science, mathematics, astronomy, ecology, art and media.\nThe Teacher Transformation programme uses constructivist, hands-on training, follow-up support and 'Make Your Own Lab' methods intended to shift classroom practice. Young Instructor Leader develops selected students as peer instructors rather than treating them only as recipients.\nThe official 2023–24 Annual Report and current programme pages provide detailed evidence on programme structure, although public reporting does not consistently publish child-level baseline-to-endline learning results for every delivery channel.",
            [
                {"label": "Official Annual Report 2023–24", "url": "https://www.agastya.org/_files/ugd/eee33c_92a5aeebcbc84ce48d9aef9ac5247acc.pdf"},
                {"label": "Official programmes page", "url": "https://www.agastya.org/programs"},
            ],
        ),
        _row(
            "Agastya documents a varied set of recurring opportunities beyond ordinary classroom instruction. Young Instructor Leaders teach peers and take visible responsibility; students design prototypes and present them through science and innovation fairs; selected projects enter national and international competitions; and Anveshana pairs schoolchildren with engineering students to co-create solutions. The campus model also gives children exposure to astronomy, ecology, art and media, while residential and day camps extend participation beyond a single demonstration.\nThe 2023–24 report records eight mega science fairs, ten mini science fairs, twelve innovation fairs and about 80 prototypes, with additional campus projects selected for competitions. These are public platforms, mentorship relationships, leadership roles and project pathways rather than generic extracurricular claims.\nMeals, transport and access to laboratory infrastructure are not counted here by themselves. The Development Environment evidence rests on repeated peer leadership, creation, mentorship, public presentation, competitions and cross-disciplinary exposure documented in the official report.",
            [
                {"label": "Official Annual Report 2023–24", "url": "https://www.agastya.org/_files/ugd/eee33c_92a5aeebcbc84ce48d9aef9ac5247acc.pdf"},
                {"label": "Official programmes page", "url": "https://www.agastya.org/programs"},
            ],
        ),
    ),

    "angels_orphanage_bengaluru": _pack(
        [
            "angels orphanage", "angel orphanage", "angels orphanage bengaluru",
            "angels orphanage bangalore",
        ],
        _row(
            "The only substantive public record located was Bangalore Food Bank's official partner-organisation page, which lists Angels Orphanage at Anatha Ashram Compound in Shivaji Nagar and records 50 beneficiaries. This establishes a named institution and an approximate partner-reported beneficiary count, but not children's progression.\nNo official Angels Orphanage website, annual report, impact report, named former resident, school-completion result, college destination, family-reintegration outcome, vocational completion or employment outcome was located. The figure of 50 must not be treated as an alumni or success count.\nThe evidence pack is intentionally limited to what the partner source substantiates.",
            [
                {"label": "Bangalore Food Bank official partner list", "url": "https://bangalorefoodbank.com/partner_orgs.html"},
            ],
        ),
        _row(
            "No public evidence was located on the schools attended by residents, tutors, study schedule, curriculum, remedial instruction, assessment, mentoring, vocational preparation or transition planning. An orphanage or residential identity does not establish an educational model by itself.\nNo official website or annual or impact report for Angels Orphanage was found. The partner listing should therefore be used only to confirm the institution's name, location and listed beneficiary count, not to infer a learning pathway.",
            [
                {"label": "Bangalore Food Bank official partner list", "url": "https://bangalorefoodbank.com/partner_orgs.html"},
            ],
        ),
        _row(
            "No public evidence was found of recurring arts, sport, clubs, competitions, child leadership, external mentors, educational visits, public performances or child-led community projects for the resident cohort.\nResidence, food, protection and basic care are essential services but are not counted as Development Environment evidence. No opportunity pathway should be inferred from the word 'orphanage' or from the Bangalore Food Bank partnership alone.\nNo official annual or impact report was located.",
            [
                {"label": "Bangalore Food Bank official partner list", "url": "https://bangalorefoodbank.com/partner_orgs.html"},
            ],
        ),
    ),

    "anugraha_educational_and_social_trust": _pack(
        [
            "anugraha educational and social trust", "anugraha educational social trust",
            "anugraha trust",
        ],
        _row(
            "The official website reports broad reach figures such as 500+ students supported and 200+ people described as skilled professionals, but it does not identify named students, school completion, board results, college admission, course completion, job placement, earnings or a cohort denominator. These figures measure claimed reach and cannot be converted into progression rates.\nThe website also claims that schools have been established, while the detailed school project page describes the initiative as being in the planning stage. No public record was found linking beneficiaries to completed education or employment destinations.\nNo official annual or substantive impact report was located; assessment is based on the current official website, which contains material internal inconsistencies.",
            [
                {"label": "Official trust website", "url": "https://anugrahaeducationalandsocialtrust.com/"},
                {"label": "Official activities page", "url": "https://anugrahaeducationalandsocialtrust.com/index.php/activites/"},
                {"label": "Official programmes page", "url": "https://anugrahaeducationalandsocialtrust.com/index.php/programs/"},
            ],
        ),
        _row(
            "The official programme page describes a Skill Development and Training Center launched in February 2024, with computer literacy, tailoring and handicrafts, English communication and entrepreneurship. However, it does not publish course duration, class frequency, curriculum sequence, trainer qualifications, assessment, attendance, completion or placement conversion.\nThe proposed school for underprivileged children is explicitly presented as being planned, and its 'key activities' section duplicates healthcare content rather than describing schooling. A planned digital-literacy drive is also not credited as completed delivery.\nNo official annual or impact report was found. The public evidence supports a claimed training offer, but not a fully documented learning system or operating school.",
            [
                {"label": "Official programmes page", "url": "https://anugrahaeducationalandsocialtrust.com/index.php/programs/"},
                {"label": "Official trust website", "url": "https://anugrahaeducationalandsocialtrust.com/"},
            ],
        ),
        _row(
            "No defined child cohort is publicly shown receiving a recurring and varied set of opportunities such as arts or sport progression, clubs, public exhibitions, child leadership, sustained mentoring, educational visits or community projects.\nEntrepreneurship and communication training belong to the stated Learning Model and are not counted again as Development Environment merely because they are non-academic. General awareness programmes, volunteering and community events do not establish a child-level opportunity pathway without participants, frequency and outputs.\nNo official annual or impact report was located.",
            [
                {"label": "Official activities page", "url": "https://anugrahaeducationalandsocialtrust.com/index.php/activites/"},
                {"label": "Official programmes page", "url": "https://anugrahaeducationalandsocialtrust.com/index.php/programs/"},
            ],
        ),
    ),

    "bharath_seva_sangh_sampatthu": _pack(
        [
            "bharath seva sangh", "bharat seva sangh", "sampatthu",
            "sampatthu bharath seva sangh", "sampatthu bharat seva sangh",
        ],
        _row(
            "Sampatthu is presented as a shelter home for underprivileged boys, but the official website does not publish school grades, attendance, Class 10 or 12 completion, college entry, vocational certification, family reintegration, employment or named former-resident destinations.\nThe site separately advertises computer-application training for fresh graduates intended to improve IT employment prospects. Those participants cannot be assumed to be Sampatthu's resident children, and no resulting placements are reported.\nNo official annual or substantive impact report was located; the evidence is based on the official institution and activity pages.",
            [
                {"label": "Official Sampatthu website", "url": "https://sampatthu.org/"},
                {"label": "Official programme and activity archive", "url": "https://sampatthu.org/blog-index.php"},
            ],
        ),
        _row(
            "The official site says resident boys receive coaching in sport, crafts, music, drama and drawing, but it gives little information on their formal schooling, tutors, study timetable, academic assessment, remediation or transition preparation.\nThe separate computer-application course for fresh graduates should not be merged into the resident children's educational pathway without evidence that the same cohort participates.\nNo official annual or impact report was found. The current public evidence establishes enrichment coaching more clearly than it establishes a structured academic learning model.",
            [
                {"label": "Official Sampatthu website", "url": "https://sampatthu.org/"},
                {"label": "Official programme and activity archive", "url": "https://sampatthu.org/blog-index.php"},
            ],
        ),
        _row(
            "The official site documents a reasonably varied set of opportunities for resident children: coaching in volleyball and other sport, music, drama, drawing and crafts; interaction with mentors; monthly cultural programmes; participation in the recurring Abhyuday Aarohana event; and a documented volleyball prize. These provide artistic expression, public participation, adult relationships and competitive sport rather than only basic residential care.\nThe website does not publish a child-wise activity calendar, participation rate or progression over time, so it should not be stated that every resident receives every opportunity. Religious observances and ordinary festival celebrations are not counted by themselves.\nFood, shelter, clothing and protection are baseline residential services and are excluded from Development Environment evidence. No official annual or impact report was located.",
            [
                {"label": "Official Sampatthu website", "url": "https://sampatthu.org/"},
                {"label": "Official programme and activity archive", "url": "https://sampatthu.org/blog-index.php"},
            ],
        ),
    ),

    "bosco_bengaluru": _pack(
        [
            "bosco", "bosco bengaluru", "bosco bangalore", "boscoban",
            "bangalore oniiyavara seva coota", "bangalore oniiyavara seva koota",
        ],
        _row(
            "BOSCO Bengaluru's official Annual Report 2023–24 provides multiple destination signals. It reports 247 children receiving formal academic education across bridge school through degree level; after school, children are supported to enter colleges, ITIs or other training according to interest and aptitude. The report records 151 young people placed in jobs during the year, 32 becoming self-employed and 25 placements linked to computer training, with follow-up after placement.\nNamed pathways include Mahesh completing bakery training and joining Amma Pastries, Vani completing basic computer and Tally training and obtaining work, and Mohan progressing to Assistant Manager at Kotak Mahindra Bank. The report also records 3,653 children home-placed or reunified, which is a child-protection transition rather than an education outcome.\nThese figures arise from different BOSCO programmes and must not be merged into one success rate. The official 2023–24 Annual Report was located and read.",
            [
                {"label": "Official Annual Report 2023–24", "url": "https://boscoban.org/wp-content/uploads/2024/12/Annual-Report-Final-Copy-compressed.pdf"},
                {"label": "Official BOSCO Bengaluru website", "url": "https://boscoban.org/"},
            ],
        ),
        _row(
            "BOSCO uses a staged education and transition pathway for children who are out of school, on the street or in vulnerable circumstances. Non-formal education is described as flexible, participatory and inclusive; bridge education combines academic preparation with creative learning, mentoring and structured reintegration into formal school. Formal education support continues through school and higher education, while 27 tuition centres reportedly reached 810 children and supported re-enrolment.\nOlder youth can enter vocational courses including bakery, tailoring, welding, motor mechanics, carpentry, electrical work, beautician training and screen printing, as well as computer training, spoken English and life skills. The report links training to placement and follow-up rather than presenting skills activity alone.\nCounselling and case management support the pathway but are not treated as a teaching method by themselves. The official 2023–24 Annual Report provides the main evidence.",
            [
                {"label": "Official Annual Report 2023–24", "url": "https://boscoban.org/wp-content/uploads/2024/12/Annual-Report-Final-Copy-compressed.pdf"},
                {"label": "Official BOSCO Bengaluru website", "url": "https://boscoban.org/"},
            ],
        ),
        _row(
            "BOSCO documents a varied and recurring Development Environment. Child Rights Clubs and Child Protection Committees give children participation and civic roles; talent-enhancement, cultural and recreational programmes provide public-expression opportunities; karate and organised sport create physical-development pathways; and youth meets, exposure visits, picnics, life-skills camps and career events widen children's networks and experiences.\nThe 2023–24 report also records public campaigns, rallies, street plays and drawing competitions, a sports month involving roughly 400 children, and notable achievements including a resident girl's national rope-skipping gold medal. These are leadership, advocacy, competition, performance and exposure opportunities, not merely generic extracurricular claims.\nShelter, food, healthcare, rescue and counselling are essential baseline or protection services and are not counted here as Development Environment evidence. Evidence from BOSCO Bengaluru must not be confused with Don Bosco Child Labour Mission, Davangere.",
            [
                {"label": "Official Annual Report 2023–24", "url": "https://boscoban.org/wp-content/uploads/2024/12/Annual-Report-Final-Copy-compressed.pdf"},
                {"label": "Official BOSCO Bengaluru website", "url": "https://boscoban.org/"},
            ],
        ),
    ),

    "child_empowerment_foundation_bal_utsav": _pack(
        [
            "child empowerment foundation india", "child empowerment foundation",
            "bal utsav", "balutsav", "bal utsav foundation",
        ],
        _row(
            "Bal Utsav's school pages publish some school-level signals, including a reported 95% SSLC pass rate over a decade at Government High School Kachinakatte and historical enrolment growth at Karnataka Public School Agara. The public pages do not establish how much of these results occurred before or after Bal Utsav's intervention, and the school data is not consistently current.\nNo named alumni, college destinations, employment outcomes or child-level progression table was located. School enrolment, scholarships and infrastructure reach are access or intermediate indicators unless retention and completion are demonstrated and attributed.\nNo accessible official annual or substantive impact-report PDF was located; the evidence is based on official programme and school pages.",
            [
                {"label": "Official Bal Utsav website", "url": "https://balutsav.org/"},
                {"label": "Official Kachinakatte school page", "url": "https://balutsav.org/school/government-high-school-kachinakatte/"},
                {"label": "Official Agara school page", "url": "https://balutsav.org/school/karnataka-public-school-agara/"},
            ],
        ),
        _row(
            "Bal Utsav's iShaala and Sampoorna Shaala models focus on whole-school transformation in government schools. The official pages describe smart classrooms and digital tools, interactive and experiential pedagogy, teacher development, scholarships, WASH and multi-year implementation—approximately three to five years for iShaala and seven to eight years for Sampoorna Shaala.\nThis establishes a structured school-improvement model rather than a one-off donation. However, the public pages reviewed do not provide a common baseline-endline assessment method, child-level learning gains, teacher-observation results or year-wise progression across the school portfolio.\nInfrastructure, WASH and scholarships support access but are not teaching methods by themselves. No accessible official annual or substantive impact-report PDF was located.",
            [
                {"label": "Official iShaala programme", "url": "https://balutsav.org/bal-utsav-flagship-programs/give-now-for-ishaala/"},
                {"label": "Official Sampoorna Shaala programme", "url": "https://balutsav.org/bal-utsav-flagship-programs/give-now-for-sampoorna-shaala/"},
                {"label": "Official Bal Utsav website", "url": "https://balutsav.org/"},
            ],
        ),
        _row(
            "The public programme pages mention school spaces for sport, recreation and community engagement, and individual school pages contain historical examples of drawing and ball-badminton achievement. They do not show a common, recurring Bal Utsav pathway through which the same children receive arts, sport, leadership, mentoring, public platforms, educational travel or child-led projects.\nBal Utsav's photography exhibition gives public visibility to children's lives and aspirations, but the available page presents children mainly as subjects of the exhibition rather than clearly as photographers, curators or child leaders. It is therefore not treated as evidence of child agency.\nBuildings, playgrounds, devices, WASH and school beautification are enabling infrastructure, not Development Environment evidence by themselves. No official annual or impact-report PDF was located.",
            [
                {"label": "Official Bal Utsav website", "url": "https://balutsav.org/"},
                {"label": "Official photography exhibition page", "url": "https://balutsav.org/the-unstoppable-a-photography-exhibition-on-hope-aspirations-purpose/"},
                {"label": "Official Kachinakatte school page", "url": "https://balutsav.org/school/government-high-school-kachinakatte/"},
            ],
        ),
    ),

    "christ_special_school": _pack(
        [
            "christ special school", "christ special school bengaluru",
            "christ special school bangalore",
        ],
        _row(
            "The official site does not publish former-student employment, mainstream-school transition, board certification, independent-living destinations or a cohort-level alumni record. A 2025 hotel-management exposure programme involving three students is current training and should not be reported as completed employment.\nHistoric and current competition achievements demonstrate participation and recognition, but they are not post-programme destinations. No official annual or substantive impact report was located.",
            [
                {"label": "Official Christ Special School website", "url": "https://christspecialschool.in/"},
                {"label": "Official academics page", "url": "https://christspecialschool.in/academics/"},
                {"label": "Official hotel-management training update", "url": "https://christspecialschool.in/2025/11/07/hotel-management-training-a-new-milestone-in-vocational-training/"},
            ],
        ),
        _row(
            "Christ Special School documents a disability-specific Functional Skills Curriculum across Primary, Secondary, Pre-vocational and Vocational stages. Children are grouped by functional level and chronological age and receive individualised education plans or home-based programmes, with one-to-one and group instruction covering functional academics, communication, social and motor skills and activities of daily living.\nThe vocational stage includes practical production such as diyas, mats, paper products, clay work, cards, jewellery and envelopes. The 2025 hotel-management programme adds weekly external training in kitchen assistance, bakery and service for a small group.\nTherapy is counted here only where it supports individual communication, mobility and learning goals; it is not treated as Development Environment evidence. No official annual or impact report was found.",
            [
                {"label": "Official academics page", "url": "https://christspecialschool.in/academics/"},
                {"label": "Official hotel-management training update", "url": "https://christspecialschool.in/2025/11/07/hotel-management-training-a-new-milestone-in-vocational-training/"},
            ],
        ),
        _row(
            "The school documents recurring opportunities across sport, yoga, art, dance and public performance. Its official history records participation by 30 students in the 2017 Kalaangana inter-school event across art, yoga, dance, vocal and instrumental music and other categories, with multiple medals. Current 2025 updates document mixed-relay teams winning second prizes, showing that external sport participation remains active.\nWeekly hotel-management exposure at Christ University connects a small group of older students to external instructors and real work settings. Together, these provide competition, performance, professional exposure and varied creative and physical pathways.\nThe evidence spans different years and groups, so it should not be stated that every student receives every opportunity. Therapy, healthcare, transport and basic special-school care are excluded from this metric.",
            [
                {"label": "Official academics and achievements page", "url": "https://christspecialschool.in/academics/"},
                {"label": "Official 2025 inter-school sports update", "url": "https://christspecialschool.in/2025/07/26/inter-school-mixed-relay-competition/"},
                {"label": "Official hotel-management training update", "url": "https://christspecialschool.in/2025/11/07/hotel-management-training-a-new-milestone-in-vocational-training/"},
            ],
        ),
    ),

    "famin_educational_and_social_welfare_trust": _pack(
        [
            "famin educational and social welfare trust", "famin trust", "famin",
        ],
        _row(
            "FAMIN's official project-report archive documents distributions of school bags, books, stationery, notebooks, shoes and educational aids. These are access inputs and do not show where children subsequently progressed.\nNo named student, school return, Class 10 or 12 completion, college admission, course completion, scholarship destination or employment outcome was located. No cohort denominator or repeated follow-up is published.\nNo official annual or substantive impact report was found. The available documents are project-specific activity reports, not an organisation-wide annual outcome report.",
            [
                {"label": "Official FAMIN website", "url": "https://www.famin.in/"},
                {"label": "Official project reports archive", "url": "https://www.famin.in/project-reports/"},
            ],
        ),
        _row(
            "The public website describes education, vocational and life-skills objectives, but the documents reviewed mainly record material distributions and awareness activities. No operating learning centre, recurring class schedule, curriculum, learner grouping, assessment, teacher roster, remedial process, course completion or transition pathway is publicly documented.\nPlanned or upcoming activities are not treated as completed delivery. Providing study materials supports access but does not establish a teaching model.\nNo official annual or substantive impact report was located; the available project reports are narrower activity records.",
            [
                {"label": "Official FAMIN website", "url": "https://www.famin.in/"},
                {"label": "Official project reports archive", "url": "https://www.famin.in/project-reports/"},
                {"label": "Official upcoming projects page", "url": "https://www.famin.in/upcoming-projects-2/"},
            ],
        ),
        _row(
            "The archive contains isolated activities such as slogan writing and proposed environmental-awareness work, but it does not demonstrate a recurring and varied opportunity pathway for a defined child cohort. No sustained arts or sport progression, child clubs, public performances, leadership roles, external mentors, educational visits or child-led community projects were found.\nOne-off distributions, awareness sessions and planned sapling activities are not sufficient Development Environment evidence. Food, healthcare and material support are also excluded from this metric.\nNo official annual or impact report was located.",
            [
                {"label": "Official project reports archive", "url": "https://www.famin.in/project-reports/"},
                {"label": "Official upcoming projects page", "url": "https://www.famin.in/upcoming-projects-2/"},
            ],
        ),
    ),

    "hazari_prasad_foundation": _pack(
        [
            "hazari prasad foundation", "hazari prasad charitable foundation",
            "hazariprasad foundation",
        ],
        _row(
            "The Foundation reports scholarships for higher fine-arts education, support to artists and employment opportunities, and says thousands of underprivileged or visually impaired students and artists have benefited. The public pages do not identify named former students, course completion, institutions entered, professional placements, earnings or a cohort denominator.\nScholarship and employment language should therefore be retained as reported programme intent or reach, not converted into documented alumni destinations. No official annual or substantive impact report was located.",
            [
                {"label": "Official Foundation website", "url": "https://www.hazariprasadfoundation.com/"},
                {"label": "Official projects page", "url": "https://www.hazariprasadfoundation.com/projects.html"},
            ],
        ),
        _row(
            "The official site establishes free fine-arts education, music programmes, scholarships and artist support as core activities. It does not publish the curriculum, class frequency, course duration, instructor qualifications, learner count by age, assessment, certification or progression through levels.\nBecause the Foundation serves both students and adult artists, evidence must not automatically be attributed to a child cohort. No official annual or impact report was found.",
            [
                {"label": "Official projects page", "url": "https://www.hazariprasadfoundation.com/projects.html"},
                {"label": "Official Foundation website", "url": "https://www.hazariprasadfoundation.com/"},
            ],
        ),
        _row(
            "The Foundation says it regularly organises music events, concerts, talent shows and performances in established auditoriums, giving young and disadvantaged artists public stages and recognition. This is credible evidence of public performance and artistic exposure beyond private instruction.\nThe evidence is concentrated in fine arts and does not demonstrate a broader recurring mix of sport, child leadership, clubs, educational travel, community projects or workplace exposure. It is also unclear what proportion of participants are children rather than adult artists, and no participant-level progression is published.\nMedical assistance and general artist welfare are not counted as Development Environment evidence. No official annual or impact report was located.",
            [
                {"label": "Official events page", "url": "https://www.hazariprasadfoundation.com/events.html"},
                {"label": "Official projects page", "url": "https://www.hazariprasadfoundation.com/projects.html"},
            ],
        ),
    ),

    "international_human_development_and_upliftment_academy": _pack(
        [
            "international human development and upliftment academy", "ihdua",
            "ihdua academy", "international human development upliftment academy",
        ],
        _row(
            "IHDUA's current Mullur School page reports that more than 3,000 students have completed Class 10 since the school began and says recent pass rates have been at or near 100%. Older official annual reports provide specific cohorts: 37 of 38 SSLC students passed in 2015–16; the 2017–18 report records 52 students with a 95% pass rate; and the 2018–19 report records 35 students with a 100% pass rate.\nThese are repeated school-completion results, but the public material does not provide subsequent PUC, college, vocational, employment or named alumni destinations. The current website's 'past five years' statement should be verified against newer result records because the latest annual report located was for 2018–19.\nOfficial annual-report PDFs for 2015–16, 2017–18 and 2018–19 were located and reviewed alongside the current school pages.",
            [
                {"label": "Official Mullur School page", "url": "https://ihdua.org/rural-education/mullur-school-mysuru/"},
                {"label": "Official Annual Report 2015–16", "url": "https://ihdua.org/wp-content/uploads/2023/08/IHDUA-Annual-Report-2015.pdf"},
                {"label": "Official Annual Report 2017–18", "url": "https://ihdua.org/wp-content/uploads/2023/08/IHDUA-Annual-Report-2017.pdf"},
                {"label": "Official Annual Report 2018–19", "url": "https://ihdua.org/wp-content/uploads/2023/08/IHDUA-Annual-Report-2018.pdf"},
            ],
        ),
        _row(
            "Mullur School is a full-time rural school from kindergarten through Class 10. Official reports describe English instruction from LKG, computer education, and additional group study before and after school for academically weaker SSLC students. Adarsha Academy is reported as a smaller Kannada-medium school following the Karnataka curriculum, with English added in higher primary grades.\nThe repeated SSLC cohort results and targeted group-study support provide more concrete evidence than generic school claims. Public material is still limited on baseline assessment, level grouping below Class 10, teacher ratios, classroom observation and current learning gains.\nThe most recent annual-report PDF located was 2018–19, so current continuity of the documented practices should be confirmed from the website and school records.",
            [
                {"label": "Official Mullur School page", "url": "https://ihdua.org/rural-education/mullur-school-mysuru/"},
                {"label": "Official Adarsha Academy page", "url": "https://ihdua.org/rural-education/adarsha-academy-krs/"},
                {"label": "Official Annual Report 2018–19", "url": "https://ihdua.org/wp-content/uploads/2023/08/IHDUA-Annual-Report-2018.pdf"},
            ],
        ),
        _row(
            "IHDUA's annual reports document a varied school environment beyond core lessons: Pratibha Karanji cultural competitions, volleyball and badminton, yoga, annual-day dances and skits, science and art exhibitions, and educational excursions. The school also reports an art studio and computer laboratory. These give children competitive sport, cultural performance, public exhibition and exposure outside the classroom.\nThe strongest detailed evidence comes from annual reports between 2015–16 and 2018–19; current continuation, frequency and participation rates are not published in a recent report. The activities should therefore be described as documented institutional practice, not assumed current participation for every child.\nNutrition, healthcare and general rural-development programmes are not counted here unless they create a specific child opportunity pathway.",
            [
                {"label": "Official Annual Report 2015–16", "url": "https://ihdua.org/wp-content/uploads/2023/08/IHDUA-Annual-Report-2015.pdf"},
                {"label": "Official Annual Report 2017–18", "url": "https://ihdua.org/wp-content/uploads/2023/08/IHDUA-Annual-Report-2017.pdf"},
                {"label": "Official Annual Report 2018–19", "url": "https://ihdua.org/wp-content/uploads/2023/08/IHDUA-Annual-Report-2018.pdf"},
                {"label": "Official Mullur School page", "url": "https://ihdua.org/rural-education/mullur-school-mysuru/"},
            ],
        ),
    ),

    "namma_bhoomi_concerned_for_working_children": _pack(
        [
            "namma bhoomi", "namma bhoomi concerned for working children",
            "namma bhoomi concern for working children",
            "namma bhoomi the concerned for working children",
            "concerned for working children", "concern for working children",
            "the concerned for working children",
            "cwc namma bhoomi", "namma nalanda vidyapeetha",
            "namma nalanda vidyapeeta",
        ],
        _row(
            "The Concerned for Working Children’s 2021 Annual Report records internal assessments for 50 young people in Namma Bhoomi’s vocational programme and says 18 learners from the preceding batch were ready to graduate, although their certificate ceremony was delayed during the pandemic. This demonstrates programme completion at that point, but the report does not publish the graduates’ employers, earnings, further-study destinations or retention in work.\nAn older official report documents Namma Sabha, an association of former Namma Bhoomi trainees, and reports that more than 150 former students attended an alumni conference to share experiences, engage with current and outgoing trainees and prepare an action plan. Alumni and care leavers are also documented participating in public-policy consultations.\nThese are credible completion, alumni-network and civic-progression signals. They should not be converted into a current cohort employment rate because the public reports do not provide a recent denominator or systematic destination table. Official Annual Reports 2021 and 2013 were located and reviewed alongside the current programme page.",
            [
                {"label": "Official Annual Report 2021", "url": "https://www.concernedforworkingchildren.org/wp-content/uploads/ANNUAL-REPORT-2021.pdf"},
                {"label": "Official Annual Report 2013", "url": "https://www.concernedforworkingchildren.org/wp-content/uploads/AR2013_4Oct14_Final_Arpita.pdf"},
                {"label": "Official education and Namma Bhoomi programme page", "url": "https://www.concernedforworkingchildren.org/empowering-children/education-for-democracy/"},
            ],
        ),
        _row(
            "Namma Bhoomi combines formal academic education, life skills and vocational preparation. The official programme page describes flexible, child-centred education for younger learners and an approximately 18-month residential vocational pathway for adolescents in trades including construction, carpentry, electrification, weaving, bamboo work, tailoring and housekeeping. Learners can use NIOS and other formal certification routes.\nThe model uses practical materials, local artisans, self-directed and group learning, internal assessment and production linked to a real sales outlet through Namma Angadi. The 2021 report also describes children choosing practical modules according to interest, including gardening, cooking, public speaking, organic farming, electrical work, plumbing, computer use, dairy, first aid, cycling and marketing.\nThis is a structured bridge between academic learning, occupational skills and transition preparation. The public evidence is less clear on current learner-level baselines, completion rates across recent cohorts and placement conversion. Official Annual Reports 2021 and 2013 were reviewed.",
            [
                {"label": "Official education and Namma Bhoomi programme page", "url": "https://www.concernedforworkingchildren.org/empowering-children/education-for-democracy/"},
                {"label": "Official Annual Report 2021", "url": "https://www.concernedforworkingchildren.org/wp-content/uploads/ANNUAL-REPORT-2021.pdf"},
            ],
        ),
        _row(
            "Namma Bhoomi and CWC document an unusually varied and recurring opportunity environment. Children elect a Makkala Panchayat with office bearers; working children organise through Bhima Sangha; and children use Makkala Gram Sabhas and Children’s Post Boxes to raise issues with local government and follow up on action. Young people and care leavers have also spoken at national press conferences and participated in UNICEF, ILO and other policy consultations.\nThe reports additionally document Yakshagana, singing, dancing, storytelling, art, craft and fine-arts competitions, together with public speaking and alumni interaction. This provides child leadership, civic agency, public platforms, cultural performance and intergenerational mentoring rather than one narrow extracurricular activity.\nFood, shelter, residential care, healthcare and routine schooling are not counted as Development Environment evidence. Some examples span different locations and years, so the pack does not assume that every Namma Bhoomi learner receives every opportunity. Official Annual Reports 2021 and 2013 were reviewed.",
            [
                {"label": "Official Annual Report 2021", "url": "https://www.concernedforworkingchildren.org/wp-content/uploads/ANNUAL-REPORT-2021.pdf"},
                {"label": "Official Annual Report 2013", "url": "https://www.concernedforworkingchildren.org/wp-content/uploads/AR2013_4Oct14_Final_Arpita.pdf"},
                {"label": "Official CWC website", "url": "https://www.concernedforworkingchildren.org/"},
            ],
        ),
    ),

    "prashanthi_balamandira_trust": _pack(
        [
            "prashanthi balamandira trust", "prasanthi balamandira trust",
            "pbmt", "pbt", "sri sathya sai loka seva gurukulam",
            "sathya sai loka seva gurukulam", "prashanti balamandira trust",
        ],
        _row(
            "The official Gurukulam page describes a pathway from Grade 6 through undergraduate study, followed by internships and possible postgraduate or doctoral continuation. The downloadable official report currently available through PBMT’s report page is titled Annual Report 2022–23, even though the website also labels links as 2023–24 and 2024–25; those current-year links resolve to the older file and should not be treated as newer evidence.\nThe 2022–23 report presents named first-generation graduates, including Vithya and Nikethan, and describes Akilan completing a BSc before an institutional internship involving finance, management, teaching and mentoring. It also reports that roughly half of graduate students are first-generation graduates and records 17 gold medallists across the first two convocations, 11 of them women.\nThese are substantial higher-education completion and transition signals, but the report does not provide a complete school-entry cohort denominator, a recent college-completion rate or a verified employment table. Internship and ‘ready employment’ pathways must not be reported as completed employment unless a destination is explicitly shown.",
            [
                {"label": "Official annual reports page", "url": "https://www.pbmt.org/annual-report"},
                {"label": "Official downloadable Annual Report 2022–23", "url": "https://www.pbmt.org/_files/ugd/eed9e2_b72c4bf7359a4569b6e705630a73b31b.pdf"},
                {"label": "Official higher-primary and secondary Gurukulam page", "url": "https://www.pbmt.org/higher-primary-secondary-sri-sathya-loka-seva-gurukulam"},
            ],
        ),
        _row(
            "PBMT describes a continuous, free educational system spanning school, university, internship and further study. Its stated model combines child-centred integral education, the Head–Heart–Hand framework and four capacities—critical thinking, creativity, communication and collaboration—with academic teaching and life skills.\nThe 2022–23 report documents a Future Ready Academy covering practical skills such as gardening, cooking, carpentry, plumbing, electrical work, driving, accounting and finance; one- to two-year institutional internships after undergraduate study; stipends for selected master’s students; and an Integrated Rural Development curriculum combining theory with approximately 20 practical village hours.\nThis is a defined transition-oriented learning model rather than generic ‘holistic education.’ Public evidence is still limited on assessment methods and learner-level academic gains across campuses. The report-page labelling issue remains material: the downloadable file reviewed is 2022–23, not a verified 2024–25 report.",
            [
                {"label": "Official higher-primary and secondary Gurukulam page", "url": "https://www.pbmt.org/higher-primary-secondary-sri-sathya-loka-seva-gurukulam"},
                {"label": "Official downloadable Annual Report 2022–23", "url": "https://www.pbmt.org/_files/ugd/eed9e2_b72c4bf7359a4569b6e705630a73b31b.pdf"},
                {"label": "Official annual reports page", "url": "https://www.pbmt.org/annual-report"},
            ],
        ),
        _row(
            "The documented opportunity environment includes practical village engagement through the Integrated Rural Development curriculum, community-service expectations, arts- and skills-based courses, alumni-led ‘Each One Educate One’ activity, and campus internships that give older learners responsibility in teaching, mentoring, finance and administration. Convocations and institutional events also create public recognition and interaction with professionals from education, science, culture and public life.\nThis provides community participation, applied responsibility, peer or alumni contribution, creative pathways and professional exposure. However, several examples relate to university students and interns rather than every school-age child, so they must be attributed to the relevant cohort.\nFree residence, food, healthcare, spiritual instruction and ordinary academic provision are not counted as Development Environment evidence. The latest downloadable annual report verified was 2022–23 despite newer labels on the reports page.",
            [
                {"label": "Official downloadable Annual Report 2022–23", "url": "https://www.pbmt.org/_files/ugd/eed9e2_b72c4bf7359a4569b6e705630a73b31b.pdf"},
                {"label": "Official higher-primary and secondary Gurukulam page", "url": "https://www.pbmt.org/higher-primary-secondary-sri-sathya-loka-seva-gurukulam"},
                {"label": "Official annual reports page", "url": "https://www.pbmt.org/annual-report"},
            ],
        ),
    ),

    "right_to_play_foundation_india": _pack(
        [
            "right to play foundation", "right2play foundation",
            "right to play foundation india", "right 2 play foundation",
            "right2play", "right to play",
        ],
        _row(
            "The local Bengaluru organisation’s official website profiles two current young badminton participants: Pratheesh is described as training at a partner academy under an elite coach, while Venu is a beginner. These are current participation or training pathways, not alumni destinations.\nThe website claims that 85% of participating children show improved attendance and academics, but it does not publish the cohort size, baseline, comparison method, measurement period or underlying results. It also does not document school completion, higher education, professional sports entry, employment or repeated former-participant destinations.\nNo official annual or substantive impact-report PDF was located for this Bengaluru foundation. Evidence from the separate international organisation called Right To Play has not been imported.",
            [
                {"label": "Official local Foundation website", "url": "https://www.right2play.in/"},
                {"label": "Official participant stories", "url": "https://www.right2play.in/stories.html"},
                {"label": "Official impact page", "url": "https://www.right2play.in/impact.html"},
            ],
        ),
        _row(
            "The official site describes badminton and multi-sport exposure, coaching partnerships and an ‘AfterSport’ stream that sends weekly financial-education content through WhatsApp and may provide athlete grants. The Pratheesh profile shows one child reaching ongoing academy training.\nThe public material does not set out a sequenced sports curriculum, session frequency by cohort, coach-to-child ratio, fitness or skill assessments, progression levels, competition calendar or learning results. Grant ranges and large reach counters are also not supported by an accessible report or beneficiary table.\nNo official annual or substantive impact-report PDF was found. The pack therefore retains only the programme elements demonstrably described on the local organisation’s website.",
            [
                {"label": "Official impact page", "url": "https://www.right2play.in/impact.html"},
                {"label": "Official participant stories", "url": "https://www.right2play.in/stories.html"},
                {"label": "Official local Foundation website", "url": "https://www.right2play.in/"},
            ],
        ),
        _row(
            "Sport is the organisation’s core instructional intervention and is not counted again merely as Development Environment. The clearest additional evidence is limited to a one-day academy visit and one participant’s exposure to an elite badminton academy and coach.\nThe public website does not demonstrate a recurring and varied set of child leadership roles, public competitions, arts or cultural platforms, educational visits, civic projects, clubs, workplace exposure or long-term external mentoring for a defined cohort. Generic confidence, teamwork and resilience claims are not sufficient without programme detail.\nFood, grants, equipment, facilities and ordinary coaching inputs are not counted as Development Environment evidence. No official annual or impact-report PDF was located.",
            [
                {"label": "Official participant stories", "url": "https://www.right2play.in/stories.html"},
                {"label": "Official impact page", "url": "https://www.right2play.in/impact.html"},
            ],
        ),
    ),

    "savera_homes_basera_childrens_village": _pack(
        [
            "savera homes", "savera homes trust", "basera children's village",
            "basera childrens village", "basera children village",
            "savera basera children's village", "savera basera childrens village",
        ],
        _row(
            "Savera Homes’ official website establishes an operating residential programme for vulnerable girls, but it does not publish named former residents, Class 10 or 12 completion, college admission, vocational completion, employment, family reintegration or independent-living destinations.\nCurrent educational support, arts, sports and Teen Talk participation are programme experiences, not alumni progression. No cohort-level retention or destination table was found.\nNo official annual or substantive impact-report PDF was located. The evidence pack therefore does not infer outcomes from the presence of a residential facility, school support or donor-facing statements.",
            [
                {"label": "Official Savera Homes website", "url": "https://www.saverahomes.org/"},
                {"label": "Official About page", "url": "https://www.saverahomes.org/about-us"},
                {"label": "Official Basera Children’s Village LinkedIn page", "url": "https://in.linkedin.com/company/basera-children%E2%80%99s-village"},
            ],
        ),
        _row(
            "The official About page describes full-time educational counsellors or teachers, a library, reading room and computer room, while the home page says residents’ education is supported. These establish educational inputs around the residential cohort.\nThe public material does not specify the schools attended, curriculum, tutoring timetable, learner grouping, assessment, remedial methods, Class 10 or 12 preparation, teacher-to-child ratio or transition planning. Teen Talk webinars are developmental exposure rather than a core academic methodology.\nNo official annual or substantive impact-report PDF was found, so the current learning model cannot be assessed beyond the stated staffing and facilities.",
            [
                {"label": "Official About page", "url": "https://www.saverahomes.org/about-us"},
                {"label": "Official Savera Homes website", "url": "https://www.saverahomes.org/"},
                {"label": "Official Basera Children’s Village LinkedIn page", "url": "https://in.linkedin.com/company/basera-children%E2%80%99s-village"},
            ],
        ),
        _row(
            "Savera’s website identifies arts and sports as interest-development pathways and lists recent sports, Children’s Day, awareness and training activities. The organisation’s official LinkedIn page documents an ongoing Teen Talk series with external speakers, including a senior IPS officer, a university researcher and an adolescent-health specialist. These create sport and cultural opportunities, career or public-service exposure and recurring expert-led discussion for teenagers.\nThe evidence is still limited on frequency, participant numbers, child leadership, external competitions, public performances, educational travel and progression through an identified interest. The pack therefore does not state that every resident receives a broad programme.\nResidence, family-style care, food, counselling, healthcare and physical facilities are not counted as Development Environment evidence. No official annual or impact-report PDF was located.",
            [
                {"label": "Official Savera Homes website", "url": "https://www.saverahomes.org/"},
                {"label": "Official Basera Children’s Village LinkedIn page", "url": "https://in.linkedin.com/company/basera-children%E2%80%99s-village"},
                {"label": "Official About page", "url": "https://www.saverahomes.org/about-us"},
            ],
        ),
    ),

    "shri_b_d_tatti_memorial_charitable_trust": _pack(
        [
            "shri b d tatti memorial charitable trust",
            "sri b d tatti memorial charitable trust",
            "shri bd tatti memorial charitable trust",
            "b d tatti memorial charitable trust", "bd tatti memorial charitable trust",
            "b d tatti trust", "bd tatti trust", "shri b d tatti trust",
        ],
        _row(
            "The Trust’s official Annual Report 2022–23 reports that nine students with hearing impairment joined PUC at Bangalore Oceanic College. It also reports 24 students appearing for school finals with an 87.05% result and gives cumulative figures of 105 children mainstreamed from oral-deaf education. A named case describes Seema entering a regular school after two years of speech-focused preparation.\nThese provide school certification, mainstreaming and post-secondary transition evidence. The annual report’s 87.05% result is not accompanied by a clearly stated pass-count calculation, and the cumulative mainstreaming figure spans years, so neither should be converted into a current cohort rate.\nThe 2022–23 annual report was opened and visually reviewed. The official reports archive also contains older annual and project reports; cohorts and years must remain separate.",
            [
                {"label": "Official Annual Report 2022–23", "url": "https://bdtatti.org/wp-content/uploads/2021/02/BD-Tatti-Annual-Report-2023-3.pdf"},
                {"label": "Official reports archive", "url": "https://bdtatti.org/reports/"},
                {"label": "Official Trust website", "url": "https://bdtatti.org/"},
            ],
        ),
        _row(
            "The 2022–23 report describes a disability-specific pathway using total communication, hearing-aid support, auditory monitoring, audio-verbal training, functional English, smart classrooms, science and technology laboratories, teacher training and structured early intervention. Its preschool programme is intended to prepare children for mainstream education, while the residential school combines academic and functional preparation for further study and work.\nThe report distinguishes oral-deaf education, residential schooling, primary intervention and skill training, but its public data do not provide individual education-plan achievement rates, assessment instruments, instructional frequency by cohort or recent employment conversion. Therapy is counted here only where it supports communication, learning and transition goals.\nThe official Annual Report 2022–23 was reviewed alongside the reports archive and current website.",
            [
                {"label": "Official Annual Report 2022–23", "url": "https://bdtatti.org/wp-content/uploads/2021/02/BD-Tatti-Annual-Report-2023-3.pdf"},
                {"label": "Official reports archive", "url": "https://bdtatti.org/reports/"},
                {"label": "Official Trust website", "url": "https://bdtatti.org/"},
            ],
        ),
        _row(
            "The 2022–23 annual report documents regular yoga and sport, including Mallakhamba, and shows participation in activities such as Quizabled. These offer physical progression and an external knowledge platform beyond classroom instruction.\nPublic evidence is much thinner on a varied current pathway across arts, public performance, child leadership, educational visits, community projects, external mentors and market-facing production. Images or isolated mentions are not treated as proof that all children participate regularly.\nResidential care, food, hearing aids, therapy, medical support and ordinary school facilities are not counted as Development Environment evidence. The official Annual Report 2022–23 was visually reviewed.",
            [
                {"label": "Official Annual Report 2022–23", "url": "https://bdtatti.org/wp-content/uploads/2021/02/BD-Tatti-Annual-Report-2023-3.pdf"},
                {"label": "Official reports archive", "url": "https://bdtatti.org/reports/"},
            ],
        ),
    ),

    "snehadeep_trust_for_the_disabled": _pack(
        [
            "snehadeep trust for the disabled", "snehadeep trust",
            "sneha deep trust for the disabled", "sneha deep trust",
            "snehadeep", "snehadeep trust disabled",
        ],
        _row(
            "Snehadeep’s official Annual Report 2024–25 gives two named employment destinations: Lakshmi is reported to have obtained a data-entry role and Sukruth a front-desk executive role. The organisation’s homepage also carries broad cumulative claims of thousands trained and 595 people placed in corporate jobs, but those counters do not provide the relevant years, cohort denominator, roles or retention and should not be treated as a verified placement rate.\nThe named stories demonstrate employment progression for individual learners with visual impairment. The public report does not provide a complete annual placement table, salary information, job retention or school-to-college destinations.\nThe official Annual Report 2024–25 was located and read alongside the current programme pages.",
            [
                {"label": "Official Annual Report 2024–25", "url": "https://www.snehadeep.org/documents/annual_report24-25.pdf"},
                {"label": "Official transparency and reports page", "url": "https://www.snehadeep.org/transparency.php"},
                {"label": "Official Snehadeep website", "url": "https://www.snehadeep.org/"},
            ],
        ),
        _row(
            "The 2024–25 report documents computer-literacy training for 120 visually impaired students, including screen-reader use through JAWS and NVDA, typing, email, internet and Microsoft Office. It also describes spoken English, public speaking, resume preparation, mock interviews, workplace etiquette and mentor interaction.\nThe current programme page adds orientation and mobility, assistive-technology learning and vocational preparation. These form a coherent accessibility-to-employment pathway rather than generic computer exposure.\nThe public material does not provide entry and exit assessments, course-completion rates, hours per learner or placement conversion by training cohort. Rehabilitation and assistive support are counted here only when linked to functional learning and transition. The official Annual Report 2024–25 was reviewed.",
            [
                {"label": "Official Annual Report 2024–25", "url": "https://www.snehadeep.org/documents/annual_report24-25.pdf"},
                {"label": "Official What We Do page", "url": "https://www.snehadeep.org/whatwedo.php"},
                {"label": "Official transparency and reports page", "url": "https://www.snehadeep.org/transparency.php"},
            ],
        ),
        _row(
            "Snehadeep documents a varied opportunity environment. Its cultural group trains participants in traditional and folk dance, vocal and instrumental music and has performed in India, the United States and the United Kingdom. The 2024–25 report records educational trips, national-festival speeches and cultural programmes, Gandhi Jayanti cleanliness drives and peace marches, public awareness and school or college engagement, and interaction with professional mentors.\nThese provide public performance, educational travel, civic participation, advocacy, external mentoring and public-speaking opportunities. The Prakruti Snehi paper-recycling initiative also links environmental action and disability employment, although participant age and cohort attribution should be checked.\nLodging, healthcare, aids, counselling and routine rehabilitation are not counted as Development Environment evidence. The official Annual Report 2024–25 was reviewed.",
            [
                {"label": "Official Annual Report 2024–25", "url": "https://www.snehadeep.org/documents/annual_report24-25.pdf"},
                {"label": "Official What We Do page", "url": "https://www.snehadeep.org/whatwedo.php"},
            ],
        ),
    ),

    "spastics_society_of_karnataka": _pack(
        [
            "spastics society of karnataka", "the spastics society of karnataka",
            "spastics society karnataka", "ssk bengaluru", "ssk bangalore",
        ],
        _row(
            "SSK’s official success stories document several substantial individual pathways. Vipin completed Classes 10 and 12 through NIOS, earned a BA in Public Administration and has worked as an administrative assistant in a multinational company for roughly two decades. Vishnu completed NIOS Secondary and Senior Secondary, a Media Studies degree and a postgraduate journalism diploma before becoming a sub-editor at Firstpost. Latha is reported to work at Mindtree and to run an edible-oil business with her family.\nThese are named education-to-employment and entrepreneurship destinations, but they are individual stories rather than a cohort outcome rate. The public pages do not publish annual completion, placement or job-retention tables.\nSSK’s official annual-reports page lists a 2024–25 report and earlier reports, but the embedded current PDF could not be reliably opened and read during this review. Outcome evidence therefore comes from current official programme and success-story pages rather than unverified report content.",
            [
                {"label": "Official annual reports page", "url": "https://www.spasticssocietyofkarnataka.org/about-us/annual-reports"},
                {"label": "Official Vipin success story", "url": "https://www.spasticssocietyofkarnataka.org/about-us/success-stories/vipin-janardhanan"},
                {"label": "Official Latha success story", "url": "https://www.spasticssocietyofkarnataka.org/about-us/success-stories/latha"},
                {"label": "Official social-impact page with Vishnu’s pathway", "url": "https://www.spasticssocietyofkarnataka.org/about-us/social-impact"},
            ],
        ),
        _row(
            "SSK’s education pathway includes multisensory and play-based early education, functioning-level assessment, individual sessions, level-based early learning, special education, life skills, pre-vocational preparation and an accredited NIOS route covering Open Basic Education, Secondary and Senior Secondary. The Learners’ Centre adjusts instruction to the learner’s pace and functioning level.\nThe vocational stream includes data entry, visual design, visual arts, catering and baking, while sheltered-work training is designed to build work routines, social skills and readiness for supported employment. The official social-impact page also describes assessment, IEP planning, NIOS documentation and examination accommodation.\nThis is a differentiated education-to-work model. Therapy is counted only where it supports functional learning and individual plans. The 2024–25 annual report is listed officially but its embedded PDF was not reliably readable, so this pack relies on official programme pages.",
            [
                {"label": "Official education page", "url": "https://www.spasticssocietyofkarnataka.org/services/education"},
                {"label": "Official skill-training page", "url": "https://www.spasticssocietyofkarnataka.org/services/skill-training"},
                {"label": "Official social-impact page", "url": "https://www.spasticssocietyofkarnataka.org/about-us/social-impact"},
                {"label": "Official annual reports page", "url": "https://www.spasticssocietyofkarnataka.org/about-us/annual-reports"},
            ],
        ),
        _row(
            "SSK’s education page documents sports, art, music, clay and pottery, gardening, field visits, yoga, educational trips and an annual inclusive summer camp. Its product programme gives children and vocational trainees market-facing creative work in jute, textiles, block printing, paper, wood, screen printing, bakery and food products, including artwork used on cards sold to the public. Vipin’s story also shows an alumnus using a public platform for disability-rights advocacy.\nTogether, these provide creative production, real customer exposure, sport and arts, educational visits, inclusive group activity and civic voice. The website does not show participation frequency or demonstrate that every learner receives the entire mix, so cohort attribution must remain cautious.\nTherapy, diagnostics, counselling, medical screening and basic care are not counted as Development Environment evidence. The current annual report is listed but was not reliably readable; this section uses official programme and story pages.",
            [
                {"label": "Official education page", "url": "https://www.spasticssocietyofkarnataka.org/services/education"},
                {"label": "Official products page", "url": "https://www.spasticssocietyofkarnataka.org/connect-and-support/products"},
                {"label": "Official Vipin success story", "url": "https://www.spasticssocietyofkarnataka.org/about-us/success-stories/vipin-janardhanan"},
                {"label": "Official annual reports page", "url": "https://www.spasticssocietyofkarnataka.org/about-us/annual-reports"},
            ],
        ),
    ),

    "sri_suresh_guruji_seva_trust": _pack(
        [
            "sri suresh guruji seva trust", "sree suresh guruji seva trust",
            "sri suresh gurukula", "sree suresh gurukula", "suresh gurukula",
            "sri suresh guruji trust",
        ],
        _row(
            "Sri Suresh Gurukula is an early-childhood institution serving playgroup through Senior KG. Because the programme began only around 2020–21 and serves children approximately three to six years old, no alumni or long-term progression outcome should be inferred.\nThe official website does not publish school-readiness assessments, transition into primary school, attendance, retention, named former students or subsequent school destinations. Parent testimonials on the site are generic and appear templated, so they are not treated as outcome evidence.\nNo official annual or substantive impact-report PDF was located. The evidence is based on the Trust’s current programme, curriculum and About pages.",
            [
                {"label": "Official Sri Suresh Gurukula website", "url": "https://sureshgurukula.com/"},
                {"label": "Official About page", "url": "https://sureshgurukula.com/about-us/"},
                {"label": "Official Nursery programme page", "url": "https://sureshgurukula.com/programs-nursery/"},
            ],
        ),
        _row(
            "The Nursery programme sets out a structured multilingual curriculum in Kannada, Hindi and English. It includes letter recognition and phonics, early writing, storytelling and rhymes, counting and number concepts, shapes, pattern recognition and introductory operations using objects and pictures. The model also uses art, craft, music, dance, role play, movement, puzzles and hands-on play to develop language, cognition, social interaction and motor skills.\nThis is more specific than generic kindergarten language, but the website does not publish daily or weekly timetables, class size, learner assessment, teacher qualifications, attendance, developmental baselines or transition results. The counters on the website render as zero and should not be used as operating-scale evidence.\nNo official annual or substantive impact-report PDF was found; the learning evidence comes from official programme and curriculum pages.",
            [
                {"label": "Official Nursery programme page", "url": "https://sureshgurukula.com/programs-nursery/"},
                {"label": "Official Sri Suresh Gurukula website", "url": "https://sureshgurukula.com/"},
                {"label": "Official About page", "url": "https://sureshgurukula.com/about-us/"},
            ],
        ),
        _row(
            "Art, craft, music, dance, drama, movement, yoga and festival learning are embedded within the early-childhood curriculum and therefore are primarily part of the Learning Model, not automatically a separate Development Environment. The Events page mentions sports days, art exhibitions and cultural events as intended opportunities, but currently displays ‘No events found’ and provides no dated participant evidence.\nNo recurring external competitions, public performances, educational visits, child leadership, community projects, external mentors or sustained exposure pathway was publicly demonstrated. Generic ‘holistic development’ and facility language are not sufficient.\nFood, care, spirituality and normal kindergarten activities are not counted as Development Environment evidence. No official annual or impact-report PDF was located.",
            [
                {"label": "Official events page", "url": "https://sureshgurukula.com/events-list/"},
                {"label": "Official Nursery programme page", "url": "https://sureshgurukula.com/programs-nursery/"},
                {"label": "Official About page", "url": "https://sureshgurukula.com/about-us/"},
            ],
        ),
    ),

    "sukanksha_charitable_trust": _pack(
        [
            "sukanksha charitable trust", "sukansha charitable trust",
            "sukanksha trust", "sukansha trust", "sukanksha madilu",
        ],
        _row(
            "Sukanksha’s current official website reports 57 resident children—30 girls aged approximately 6–16 and 27 boys aged approximately 10–16—receiving shelter and access to education. These are current reach figures, not progression outcomes.\nNo named child, Class 10 or 12 result, school completion, college admission, vocational certification, employment, family reintegration or independent-living destination was found. The site’s stated aim of helping children become independent is prospective and must not be reported as achieved progression.\nNo official annual or substantive impact-report PDF was located. The pack relies on the current official website and does not infer outcomes from residential care or programme intentions.",
            [
                {"label": "Official current Sukanksha website", "url": "https://www.sukankshacharitabletrust.org/"},
                {"label": "Official legacy Sukanksha website", "url": "https://www.sukankshatrust.com/"},
            ],
        ),
        _row(
            "The official website states that the boys’ and girls’ homes provide educational support, but it does not identify schools attended, teachers or tutors, study schedules, curriculum, remedial instruction, assessment, board preparation, skills courses or transition planning.\nA proposed Ranga Madilu project is intended to use drama and acting workshops for communication and creative expression. The site explicitly says this project is in its early stages, so it cannot be treated as an established learning pathway or completed outcome.\nNo official annual or substantive impact-report PDF was found. Shelter, food and access to school are important services but do not by themselves establish a differentiated Learning Model.",
            [
                {"label": "Official current Sukanksha website", "url": "https://www.sukankshacharitabletrust.org/"},
                {"label": "Official legacy Sukanksha website", "url": "https://www.sukankshatrust.com/"},
            ],
        ),
        _row(
            "Ranga Madilu is intended to introduce children to drama, acting, creativity and communication through workshops, which could create a public-performance pathway. However, the official website says the project is still in its early stages and does not publish participant numbers, dates, frequency, productions or public performances.\nNo demonstrated recurring mix of sport, arts progression, child leadership, educational visits, external mentors, competitions, civic projects or public platforms was found for the resident cohort. Visitor celebrations and donation activities are not sufficient Development Environment evidence.\nResidence, food, emotional care, medical support and ordinary access to education are not counted under this metric. No official annual or impact-report PDF was located.",
            [
                {"label": "Official current Sukanksha website", "url": "https://www.sukankshacharitabletrust.org/"},
                {"label": "Official legacy Sukanksha website", "url": "https://www.sukankshatrust.com/"},
            ],
        ),
    ),

    "swapaksh_learning_foundation": _pack(
        [
            "swapaksh learning foundation", "swapaksh foundation",
            "swapaksh", "swapaksh education foundation",
        ],
        _row(
            "Swapaksh’s official website gives one named progression case: Ripan Pegu, an early participant, was supported to settle into regular learning and passed the NIOS Secondary Examination in June 2023. This is a concrete school-certification outcome.\nThe site does not publish the total number attempting NIOS, grade promotion, attendance change, formal-school placement, Class 12 progression, college admission or employment. The organisation reports serving about 80 children aged five to 15 with 10 paid staff and five volunteer teachers, but this is an operating-scale claim rather than an outcome denominator.\nNo official annual or substantive impact-report PDF was located. The pack therefore treats Ripan as an individual story, not a cohort success rate.",
            [
                {"label": "Official Swapaksh website and Ripan story", "url": "https://swapaksh.org/"},
                {"label": "Official organisational story", "url": "https://swapaksh.org/our-story-2/"},
                {"label": "Official 2021 programme update", "url": "https://swapaksh.org/2021-2/"},
            ],
        ),
        _row(
            "Swapaksh operates a centre for children aged roughly five to 15 with five classrooms, paid and volunteer teachers and a history of English classes delivered with U&I. Ripan’s pathway shows that the centre can prepare at least some older learners for NIOS Secondary certification, while the organisation’s story documents sustained follow-up to bring an irregular learner into a school routine.\nThe public website does not explain the complete curriculum, daily timetable, entry assessment, level grouping, class frequency by age, learning-gain measurement, NIOS preparation process or teacher qualifications. The current narrative supports a recurring learning centre, but not a fully specified pedagogy.\nNo official annual or substantive impact-report PDF was found. Transport and meals are access supports and are not treated as the Learning Model.",
            [
                {"label": "Official Swapaksh website", "url": "https://swapaksh.org/"},
                {"label": "Official organisational story", "url": "https://swapaksh.org/our-story-2/"},
                {"label": "Official About page", "url": "https://swapaksh.org/about-us-new/"},
            ],
        ),
        _row(
            "Swapaksh’s official story documents a sports programme intended to identify children’s abilities and marathon training for students. Ripan’s profile also records interests in music and rap, but it does not show that these interests were developed through a structured public-performance pathway. Volunteers from varied backgrounds provide adult interaction, although the website does not describe sustained individual mentoring.\nThe public evidence does not yet establish a varied recurring environment across competitions, arts performances, educational visits, child leadership, community projects, clubs or career exposure. A sports programme alone is not sufficient to infer a broad Development Environment.\nMeals, transport, safe facilities and ordinary teaching support are not counted under this metric. No official annual or impact-report PDF was located.",
            [
                {"label": "Official organisational story", "url": "https://swapaksh.org/our-story-2/"},
                {"label": "Official Swapaksh website", "url": "https://swapaksh.org/"},
                {"label": "Official About page", "url": "https://swapaksh.org/about-us-new/"},
            ],
        ),
    ),

    "jss_karnataka_open_school": _pack(
        ["jss karnataka open school", "jss kos", "karnataka open school jss", "jss open school"],
        _row(
            "The official JSS KOS page reports that from 1999–2000 to 2021–22, 104,197 learners enrolled and 70,069 passed, a cumulative 67.25% pass rate. In 2021–22, 1,843 learners appeared and 1,102 passed, or 59.79%. The resulting Karnataka board certificate is equivalent to regular SSLC and can support higher education or employment. These are substantial completion outcomes, although the website does not disaggregate results by age, vulnerability, study centre or later destination. No dedicated current JSS KOS annual or impact-report PDF was located; the figures come from the official programme page and should be dated to the period shown.",
            [{"label": "Official JSS KOS programme and results page", "url": "https://jssonline.org/our-institutions/general-education/jss-kos-open-school/"}],
        ),
        _row(
            "JSS KOS is a structured open-school pathway for learners aged 15 and above who left or could not access regular schooling. Learners can choose subjects and examination timing; study centres provide printed self-learning material, audio-video content, Tutor Marked Assignments, counselling and 30 compulsory Personal Contact Programme classes per subject, with additional practical sessions. The Karnataka board conducts annual and supplementary examinations, and learners can use up to six attempts within three years. This is a clearly specified flexible completion model, though the public page does not provide current learning-gain data or centre-level quality assurance. No dedicated current JSS KOS annual or impact-report PDF was located.",
            [{"label": "Official JSS KOS programme and learning strategy page", "url": "https://jssonline.org/our-institutions/general-education/jss-kos-open-school/"}],
        ),
        _row(
            "The official material demonstrates flexible access, counselling and study-centre support, but these are components of the Learning Model and are not automatically Development Environment evidence. No recurring child or youth leadership bodies, arts or sport pathways, public exhibitions, community projects, workplace exposure, educational visits or external mentoring system is described for JSS KOS learners. The wider JSS institutional network must not be attributed to the open-school cohort without evidence of participation. No dedicated current JSS KOS annual or impact-report PDF was located.",
            [{"label": "Official JSS KOS page", "url": "https://jssonline.org/our-institutions/general-education/jss-kos-open-school/"}],
        ),
    ),

    "nele_foundation": _pack(
        ["nele foundation", "nele homes", "nele anandadwara", "nele ananda dwara"],
        _row(
            "Nele's official impact page reports a 95% school-completion rate and 100+ alumni in employment or higher education, but it does not publish the denominator, calculation period or cohort table. It also gives multiple named pathways: Balu scored 95% in SSLC, topped his undergraduate course and entered an M.Sc. at the Central University of Puducherry with an IIT Madras internship; Nethra completed B.Com and works at Big Basket; Rathna completed PUC and a Fashion Design diploma and earns through tailoring and reception work; Parshuram completed ITI and works as an electrical technician. These are strong website-reported destinations across education, employment and entrepreneurship. No downloadable official annual or impact-report PDF was located, so the headline rates require later validation.",
            [{"label": "Official Nele impact stories", "url": "https://www.nelefoundation.org/impact-stories.php"}, {"label": "Official Nele Anandadwara home profile", "url": "https://www.nelefoundation.org/nele-anandadwara.php"}],
        ),
        _row(
            "Nele describes 25 years of structured residential care, education sponsorship, academic mentoring and skill development across several homes. The Anandadwara unit opened in 2023 for 25 boys aged 10–13 studying in Classes 5–7 at a government school; the wider impact stories show continued academic support through SSLC, PUC, degrees, ITI and postgraduate study. Vocational routes include fashion design, tailoring, robotics and electrical ITI. The website, however, does not publish a common timetable, assessment framework, tutor ratio or pathway-level completion data across homes. No downloadable official annual or impact-report PDF was located.",
            [{"label": "Official Nele impact stories", "url": "https://www.nelefoundation.org/impact-stories.php"}, {"label": "Official Nele Anandadwara page", "url": "https://www.nelefoundation.org/nele-anandadwara.php"}],
        ),
        _row(
            "The official site documents a varied set of opportunities across Nele homes: drawing and sport competitions, yoga camps, annual-day programmes and cultural activities; alumni stories also show responsibility and giving back, including Rathna training younger girls and former residents supporting Nele. These provide some public platform, skill transfer and community-role evidence beyond ordinary schooling. Attribution must remain cautious because the events span different homes and years, and the website does not show that every child receives the full mix or that activities form a measured progression pathway. Food, residence and counselling are not counted as Development Environment by themselves. No downloadable official annual or impact-report PDF was found.",
            [{"label": "Official Nele events and home page", "url": "https://www.nelefoundation.org/nele-anandadwara.php"}, {"label": "Official Nele impact stories", "url": "https://www.nelefoundation.org/impact-stories.php"}],
        ),
    ),

    "ramakrishna_mission_balakashrama": _pack(
        ["ramakrishna mission balakashrama", "ramakrishna mission balakashram", "balakashrama mangalore", "balakashrama mangaluru"],
        _row(
            "A March 2025 public notice states that Ramakrishna Mission Balakashrama has operated for about 75 years and admits meritorious, financially disadvantaged rural boys into a fully funded residential high-school pathway. The available source does not publish Class 10 or 12 results, college destinations, named alumni, employment outcomes or cohort completion rates. Admission into the programme is an access indicator, not a progression result. No current Balakashrama-specific official annual or impact-report PDF was located; evidence is limited to the programme announcement and therefore should not be expanded into unstated outcomes.",
            [{"label": "2025 Balakashrama admission and programme notice", "url": "https://www.mangalorean.com/ramakrishna-mission-offers-free-hostel-and-education-to-meritorious-rural-students/"}],
        ),
        _row(
            "The programme is described as a fully funded residential route for rural boys, with education, food and accommodation under resident monks and an emphasis on academic excellence, discipline and human values. This establishes a long-duration study environment but does not specify the affiliated schools, daily academic timetable, remedial teaching, assessment, mentoring cadence, board preparation or transition support after school. No current Balakashrama-specific official annual or impact-report PDF was found, and the available announcement should not be treated as a detailed pedagogy document.",
            [{"label": "2025 Balakashrama programme notice", "url": "https://www.mangalorean.com/ramakrishna-mission-offers-free-hostel-and-education-to-meritorious-rural-students/"}],
        ),
        _row(
            "Resident-monastic guidance and value education are described, but the public source does not demonstrate a varied recurring Development Environment through organised sport or arts progression, competitions, public performance, educational visits, child leadership, community projects, career exposure or external mentors. Discipline, food, accommodation and a serene campus are baseline residential conditions and are not counted automatically. No current Balakashrama-specific official annual or impact-report PDF was located.",
            [{"label": "2025 Balakashrama programme notice", "url": "https://www.mangalorean.com/ramakrishna-mission-offers-free-hostel-and-education-to-meritorious-rural-students/"}],
        ),
    ),

    "samarthanam_trust_for_the_disabled": _pack(
        ["samarthanam trust for the disabled", "samarthanam trust", "samarthanam", "samarthanam bellari branch"],
        _row(
            "Samarthanam's official education page reports 24,000 students supported in higher education and states that some supported learners completed studies at institutions including IIMs and obtained corporate jobs. It also reports an SCB-supported higher-education initiative reaching 3,500 students with disabilities. These are meaningful scale and destination claims, but the page does not provide a full cohort denominator, named destination table, completion rate or employment-retention data. The official site lists a 2024–25 annual report; the PDF was located but could not be reliably parsed in this research environment, so the pack does not claim report-specific figures beyond the accessible official programme pages.",
            [{"label": "Official Samarthanam education and higher-education page", "url": "https://samarthanam.org/education/"}, {"label": "Official Annual Report 2024-25 PDF", "url": "https://samarthanam.org/wp-content/uploads/2025/10/Annual-Report-2024-25.pdf"}],
        ),
        _row(
            "Samarthanam operates barrier-free residential schools following the Karnataka State syllabus and special-school pathways for children with intellectual and hearing disabilities. The model includes smart classrooms, activity-based instruction, functional academics, activities of daily living, sign-language instruction, pre-vocational and vocational learning, assistive materials, tutors and end-to-end higher-education support from enrolment through fees, accessible books, scribes and hostel support. The official page reports a 1:7 teacher-student ratio in its special-school model. Current programme pages are detailed, although comparable baseline-to-endline learning results are not publicly presented. The 2024–25 annual-report PDF was located but was not reliably readable here.",
            [{"label": "Official Samarthanam education page", "url": "https://samarthanam.org/education/"}, {"label": "Official Annual Report 2024-25 PDF", "url": "https://samarthanam.org/wp-content/uploads/2025/10/Annual-Report-2024-25.pdf"}],
        ),
        _row(
            "The official education page documents disability sport, music, dance, art workshops and cultural festivals, along with study tours, public performances and interaction with corporate volunteers, leaders and policymakers. Sporting Excellence creates an external competition pathway, while arts and cultural programmes provide public platforms beyond classroom instruction. This is varied Development Environment evidence, but programme participation and progression should be kept separate by cohort and campus. Therapy, accessible infrastructure, hostel support and healthcare are not counted under this metric by themselves. The 2024–25 annual-report PDF was located but could not be reliably parsed in this environment.",
            [{"label": "Official Samarthanam education and extracurricular page", "url": "https://samarthanam.org/education/"}, {"label": "Official Annual Report 2024-25 PDF", "url": "https://samarthanam.org/wp-content/uploads/2025/10/Annual-Report-2024-25.pdf"}],
        ),
    ),

    "seva_bharathi_mangalore": _pack(
        ["seva bharathi", "seva bharathi mangalore", "seva bharathi mangaluru", "chetana society", "infosys foundation seva bharathi campus for divyang"],
        _row(
            "The official Seva Bharathi report for 2016–18 documents operating units and beneficiary counts but does not provide school completion, mainstream-school transition, vocational certification, employment or named alumni destinations for children. It reports 100 children at Chetana Child Development Centre, 29 students at the residential school for visually impaired children and smaller disability-focused units in 2018; these are reach figures rather than progression outcomes. The current Campus for Divyang page is largely a project-development history and does not add destination evidence. The latest substantive report located was the 2016–18 biennial report, so all figures are historical rather than current.",
            [{"label": "Official Seva Bharathi Report 2016-18 PDF", "url": "https://www.chetanasociety.in/wp-content/uploads/2019/10/seva-bharathi-annual-report.pdf"}, {"label": "Official Campus for Divyang page", "url": "https://www.chetanasociety.in/infosys-foundation-seva-bharathi-campus-for-divyang/"}],
        ),
        _row(
            "The 2016–18 report describes Chetana as a weekday day-care school with classes grouped by severity of disability, general teaching, coaching and linked physiotherapy, speech and occupational therapy. Other units include a residential school for visually impaired children, a learning-disability centre, communication-development services, mobility training and vocational training. The current campus objective combines day care, skill development, general and social education, therapy and permanent-stay provision under one roof. This is a coherent disability-support structure, but public evidence on individual education plans, assessment tools, curriculum levels, transition criteria and current enrolment is limited. The newest substantive report found remains 2016–18.",
            [{"label": "Official Seva Bharathi Report 2016-18 PDF", "url": "https://www.chetanasociety.in/wp-content/uploads/2019/10/seva-bharathi-annual-report.pdf"}, {"label": "Official Campus for Divyang page", "url": "https://www.chetanasociety.in/infosys-foundation-seva-bharathi-campus-for-divyang/"}],
        ),
        _row(
            "The 2016–18 report records sports and games, art, music, dance and skating within Chetana, and interaction between children and senior citizens at another unit. These indicate a mix of creative, physical and intergenerational opportunities, but the report does not show competition levels, public performance progression, child leadership, educational visits or sustained external mentoring. Festival celebrations alone are not sufficient Development Environment evidence. Therapy, transport, meals and residential care are explicitly not counted under this metric. The evidence is historical because no newer substantive annual or impact report was located.",
            [{"label": "Official Seva Bharathi Report 2016-18 PDF", "url": "https://www.chetanasociety.in/wp-content/uploads/2019/10/seva-bharathi-annual-report.pdf"}, {"label": "Official Seva Bharathi units page", "url": "https://www.chetanasociety.in/infosys-foundation-seva-bharathi-campus-for-divyang/"}],
        ),
    ),

    "shri_laxmisen_education_society_raibag": _pack(
        ["shri laxmisen education society raibag", "sri laxmisen education society raibag", "shri mahaveer residential english medium school", "smrems raibag", "shri laxmisena education society"],
        _row(
            "The school's official 2020–21 annual report states that all AISSE candidates passed: 12 with distinction, 34 in first class and 31 in pass class, with named top scores of 90.8%, 87.2% and 84%. The 2019–20 report similarly records a 100% AISSE result with 17 distinctions, 37 first-class and 24 second-class results. These are repeated board-completion outcomes, but the site does not show PUC, college or employment destinations after Class 10. The reports are school annual-report webpages rather than downloadable PDFs and are now several years old.",
            [{"label": "Official school annual reports 2019-21", "url": "https://smemsrbg.com/annual-report/"}, {"label": "Official achievements page", "url": "https://smemsrbg.com/achievements/"}],
        ),
        _row(
            "Shri Mahaveer Residential English Medium School is a rural co-educational CBSE school spanning pre-primary, primary and secondary levels. The annual reports describe periodic and final assessment, parent-teacher review after each test, teacher training, online continuity during the pandemic and regular coaching in athletics, volleyball, kabaddi, kho-kho and taekwondo. The site publishes curriculum, timetable and academic-calendar sections, but does not provide differentiated remedial systems, baseline learning data or a clear scholarship/free-seat model for rural boarding students. The latest substantive annual-report content publicly visible is 2020–21.",
            [{"label": "Official school annual report", "url": "https://smemsrbg.com/annual-report/"}, {"label": "Official school home and programme profile", "url": "https://smemsrbg.com/"}],
        ),
        _row(
            "The 2019–20 annual report documents regular sports coaching, CBSE cluster and national-level participation, inter-school debate, essay, dance-drama and science-model competitions, Friday hobby classes in drama, music, gardening and games, student-organised celebrations and an educational tour. These create varied public, competitive, creative and exposure pathways beyond normal lessons. The evidence is not current and does not prove equal participation by all students. Boarding, ordinary school facilities and celebrations alone are not counted; the stronger evidence is the external competition, senior-student responsibility and educational-visit pathway. No newer substantive annual report was located.",
            [{"label": "Official annual report with activities", "url": "https://smemsrbg.com/annual-report/"}, {"label": "Official achievements page", "url": "https://smemsrbg.com/achievements/"}],
        ),
    ),

    "sportzvillage_foundation": _pack(
        ["sportzvillage foundation", "sportz village foundation", "sportzvillage", "sportz village"],
        _row(
            "Sportz Village Foundation's official Annual Impact Report 2026 page reports 92,770 children across 320 public schools in 13 states and names progression stories. Sonika won district gold medals in long jump, high jump and kabaddi and was selected for state representation; Yogesh moved from evening coaching into the Puzhal FC Elite Youth League; Shiv Kumar Soren set a national 100-metre record at the 2026 Khelo India National Tribal Games. A partner account also states that seven children entered training at recognised football academies after two league seasons. These are concrete sports destinations, although the report page does not publish the full conversion denominator or retention after selection.",
            [{"label": "Official Annual Impact Report 2026 page", "url": "https://sportzvillagefoundation.org/annual-impact-report-page"}, {"label": "Official Sportz Village Foundation website", "url": "https://sportzvillagefoundation.org/"}],
        ),
        _row(
            "The Foundation integrates structured sports and physical-education programmes into public schools and community centres. Its theory of change targets health, education, social-emotional competence and gender equity; the 2025–26 report page states that 126,178 sports sessions and 90 Sports Development Centres were delivered. Official partner testimony refers to a tried-and-tested curriculum, coaching methodology and impact-assessment tools, with talent identification and evening coaching leading toward elite pathways. Sport itself is the core Learning Model here, not automatically Development Environment. The full report is gated, so methodology detail and measured outcome tables could not be independently reviewed beyond the public report page.",
            [{"label": "Official Annual Impact Report 2026 page", "url": "https://sportzvillagefoundation.org/annual-impact-report-page"}, {"label": "Official initiatives and theory of change", "url": "https://sportzvillagefoundation.org/"}],
        ),
        _row(
            "Beyond routine physical education, the Sporting Excellence pathway provides district, state, national and elite-league competition, while league formats and Sports Development Centres expose selected children to specialised coaches and academies. Corporate employee-volunteering events create interaction with external adults, and official partner accounts describe leadership, coordination, confidence and team responsibility emerging through competitive play. These are public and mentoring opportunities, but they remain sport-centred rather than a broad arts, civic, travel and career-exposure ecosystem. Health benefits and ordinary sports sessions are not counted twice; the Development Environment evidence rests on external competition, talent progression and volunteer exposure. The full Annual Impact Report 2026 is access-gated.",
            [{"label": "Official Annual Impact Report 2026 page", "url": "https://sportzvillagefoundation.org/annual-impact-report-page"}, {"label": "Official Foundation website and partner testimony", "url": "https://sportzvillagefoundation.org/"}],
        ),
    ),

    "sri_chayadevi_anathashrama_trust": _pack(
        ["sri chayadevi anathashrama trust", "sri chayadevi anathashrama", "chayadevi anathashrama", "scat india", "scat mysore"],
        _row(
            "SCAT's official website gives several historical destination claims: girls formerly housed by the ashram are described as settled and leading independent lives; boys are described as being in good positions; and one former orphan educated through the ashram is reported to be living and working successfully in Muscat. These claims are too general to establish a cohort rate because names, years, education levels, occupations and denominators are not published. No official annual or substantive impact-report PDF was located, and the current website says operating costs have placed the institution under strain.",
            [{"label": "Official SCAT website", "url": "https://www.scatindia.in/"}],
        ),
        _row(
            "The official site states that resident children receive formal education and skills such as tailoring and repair work. This suggests a school-access plus vocational-exposure model, but it does not identify the schools attended, current number or ages of children, tutors, study timetable, vocational course duration, assessment, certification or transition preparation. Historical descriptions should not be assumed to reflect current programme delivery without verification. No official annual or substantive impact-report PDF was found.",
            [{"label": "Official SCAT website", "url": "https://www.scatindia.in/"}],
        ),
        _row(
            "Tailoring and repair work could create applied responsibility and livelihood exposure, but the official website does not show whether these are currently recurring, certified or connected to public exhibitions, customers or employment. No varied evidence was found for organised sport, arts performance, competitions, educational visits, child leadership, community projects or sustained external mentoring. Visits by dignitaries and birthday celebrations are not sufficient Development Environment evidence. Shelter, food and residential care are not counted automatically. No official annual or impact-report PDF was located.",
            [{"label": "Official SCAT website", "url": "https://www.scatindia.in/"}],
        ),
    ),

    "sri_takshashila_gurukul": _pack(
        ["sri takshashila gurukul", "sree takshashila gurukul", "takshashila gurukul", "sri takshashila"],
        _row(
            "The official donation page claims 5,000+ students reached across 60+ schools and 26+ communities. These are reach figures, not evidence of school completion, examination results, higher-education entry, vocational certification or employment. No named learner pathway or repeated cohort destination was found. The displayed donor leaderboard appears to be website interface content and should not be treated as audited evidence. No official annual or substantive impact-report PDF was located.",
            [{"label": "Official Sri Takshashila Gurukul donation and impact page", "url": "https://sritakshashilagurukul.com/donate"}],
        ),
        _row(
            "The website describes education, awareness, caring mentorship and future-ready skill development, with donations directed toward child sponsorship, school kits, books and study materials. It does not specify a recurring curriculum, teaching schedule, teachers, learner assessment, mentoring cadence, skill modules or the relationship between the organisation and the 60+ schools. Material support and broad mentorship language do not establish a differentiated Learning Model without implementation detail. No official annual or substantive impact-report PDF was found.",
            [{"label": "Official Sri Takshashila Gurukul website", "url": "https://sritakshashilagurukul.com/donate"}],
        ),
        _row(
            "The public material does not demonstrate recurring sport, arts, competitions, public presentations, child-led community projects, educational travel, leadership roles, workplace exposure or long-term external mentors. Generic references to holistic development, awareness and community impact are not sufficient. School kits, books and sponsorship are inputs and are not counted as Development Environment. No official annual or impact-report PDF was located.",
            [{"label": "Official Sri Takshashila Gurukul page", "url": "https://sritakshashilagurukul.com/donate"}],
        ),
    ),

    "sri_venkatappa_shanthamma_educational_trust": _pack(
        ["sri venkatappa shanthamma educational trust", "shri venkatappa shanthamma educational trust", "vset foundation", "vset educational trust"],
        _row(
            "The current website reports 50+ children, 1,000+ books and 500+ sports kits, but no Class 10 or 12 result, school continuation rate, scholarship destination, college admission, course completion, employment or named former student. The figures measure present reach or resources rather than child progression. The site was updated for 2026 and presents an extensive programme menu, but no official annual or substantive impact-report PDF was located.",
            [{"label": "Official VSET Foundation website", "url": "https://vsetfoundation.org/"}],
        ),
        _row(
            "The official site lists reading improvement, computer education, scholarships, career guidance, sports, yoga, parent education, emotional well-being, life skills and leadership. It also promises educators, volunteers and mentors. However, it does not publish programme schedules, curriculum, participant numbers by activity, assessment methods, teacher or mentor qualifications, scholarship selection, learning gains or evidence that all listed initiatives are currently operating. The available evidence is therefore a programme design and menu rather than a fully documented learning system. No official annual or substantive impact-report PDF was found.",
            [{"label": "Official VSET programmes and model", "url": "https://vsetfoundation.org/"}],
        ),
        _row(
            "Sports development, leadership and life-skills activities, environmental awareness and tree planting could create a varied Development Environment if delivered repeatedly. The website currently supplies mission-level descriptions and resource counters, but no dated competitions, public performances, child-led projects, educational visits, external mentors or participant outputs. Generic leadership and holistic-development language is not sufficient, and sports kits or tree counts do not demonstrate child agency. Scholarships, counselling and ordinary academic support are not counted here. No official annual or impact-report PDF was located.",
            [{"label": "Official VSET Foundation website", "url": "https://vsetfoundation.org/"}],
        ),
    ),

    "sundar_bharat_foundation": _pack(
        ["sundar bharat foundation", "sundarbharat foundation", "sundar bharat fdn"],
        _row(
            "Sundar Bharat Foundation reports specialised preparation for the Navodaya and Morarji Desai residential-school entrance examinations, with 23 interested Class 5 children enrolled in the described year. However, it does not publish how many sat the examinations, qualified or entered those schools. No Class 10 completion, college admission, employment or named alumni destination was found. The 120-student tuition turnout is a participation figure, not progression. No official annual or substantive impact-report PDF was located.",
            [{"label": "Official Sundar Bharat Foundation work page", "url": "https://www.sundarbharatfoundation.org/our-work"}],
        ),
        _row(
            "The Foundation runs free after-school tuition from 5–7 p.m. for about 120 students in Classes 5–10, covering Mathematics, Science and English. Students are regularly evaluated and receive remedial action; Class 10 learners have three dedicated teachers. A separate daily entrance-exam class uses past papers and pattern practice for Navodaya and Morarji Desai schools, and computer classes teach hardware, software, typing and internet use to Class 10 and older learners. This is a recurring, structured academic-support model, although learning gains, attendance and exam conversion are not published. No official annual or impact-report PDF was found.",
            [{"label": "Official Sundar Bharat Foundation programme page", "url": "https://www.sundarbharatfoundation.org/our-work"}],
        ),
        _row(
            "The official page documents summer camps with abacus, general knowledge, cursive writing, arts and crafts, competitions and certificates, along with planned outings to public sites for wider exposure. These provide creative and educational-exposure opportunities beyond regular tuition. The evidence is limited because dates, destinations, participant counts and recurrence are not consistently published, and the outings are described as planned rather than completed. Health and nutrition activity is not counted as Development Environment, and a single summer camp is not sufficient to infer a year-round ecosystem. No official annual or impact-report PDF was located.",
            [{"label": "Official Sundar Bharat Foundation work page", "url": "https://www.sundarbharatfoundation.org/our-work"}],
        ),
    ),

    "swasya_foundation": _pack(
        ["swasya foundation", "swasya", "swasya rural education foundation"],
        _row(
            "The official site reports 450+ students supported and presents a story of Meera, a 13-year-old rural learner who reportedly gained confidence and topped her class through after-school learning and mentorship. The same profile labels her a primary-school teacher, creating an unresolved timeline or attribution inconsistency that must be verified before it is treated as a completed career destination. No cohort completion, board result, college admission or employment table was found. No official annual or substantive impact-report PDF was located.",
            [{"label": "Official Swasya Foundation page", "url": "https://www.swasya.com/foundation"}],
        ),
        _row(
            "Swasya describes community-led rural education, after-school learning, mentorship, digital support and skill training for children and youth. The public page does not identify specific centres or schools, class frequency, curriculum, teacher or mentor numbers, assessment, learning-gain measures or pathway duration. Its repeated descriptions establish a stated model but not enough implementation detail to distinguish current delivery from organisational positioning. No official annual or substantive impact-report PDF was found.",
            [{"label": "Official Swasya Foundation page", "url": "https://www.swasya.com/foundation"}],
        ),
        _row(
            "Environmental education, tree planting and community participation could provide applied responsibility, while the foundation also references leadership skills and collective solutions. The site shows children planting trees and reports 4,950+ trees planted, but it does not identify child participant counts, recurring roles, public presentations, competitions, educational visits or a child-led environmental project structure. Generic community and leadership language is not sufficient. Livelihood programmes for women and adults must not be attributed to the child cohort. No official annual or impact-report PDF was located.",
            [{"label": "Official Swasya Foundation page", "url": "https://www.swasya.com/foundation"}],
        ),
    ),

    "capuchin_krishik_seva_kendra_daya": _pack(
        ["the capuchin krishik seva kendra", "capuchin krishik seva kendra", "cksk", "daya special school", "dayalbagh special school"],
        _row(
            "The official CKSK Annual Report 2020–21 records 98 enrolled children at Daya Special School and seven children being trained to appear for the SSLC board examination, but it does not report whether they later sat or passed. It also documents four children identified as school dropouts receiving counselling and encouragement to continue education in a wider project. No completed SSLC, mainstream-school transition, employment or alumni destination table was found. The report is substantive but dated 2020–21; no newer official annual report was located in this research.",
            [{"label": "Official CKSK Annual Report 2020-21 PDF", "url": "https://capuchinksk.org/CKSK%20Annual%20Report%20-2020-2021.pdf"}, {"label": "Official Daya Special School page", "url": "https://capuchinksk.org/daya.html"}],
        ),
        _row(
            "Daya Special School provides disability-specific education, daily skill training and linked physiotherapy, speech and hearing support. The 2020–21 report describes SSLC preparation beginning with reading, writing, comprehension and basic mathematics across Kannada, English, Science, Social Science and Mathematics, using games, cards and pictures. Fifteen children received vocational training in tailoring, cloth mats, bags, jewellery, candles and phenyl, with daily practice for selected craft groups. This is a differentiated academic-functional-vocational pathway, though current assessment results and IEP-level progress are not published. The newest report located was 2020–21.",
            [{"label": "Official CKSK Annual Report 2020-21 PDF", "url": "https://capuchinksk.org/CKSK%20Annual%20Report%20-2020-2021.pdf"}, {"label": "Official Daya Special School page", "url": "https://capuchinksk.org/daya.html"}],
        ),
        _row(
            "The 2020–21 report provides stronger applied-opportunity evidence than generic extracurricular language: children produced cloth mats, bags, jewellery, candles and other items that were displayed, sold to visitors and given as gifts, creating contact with real customers and public presentation. The wider CKSK child projects also document children's clubs, a children’s gram sabha where participants raised school-infrastructure and transport issues, creative competitions and issue-based child committees. These cohorts should not be merged automatically with Daya's 98 students, but they show organisational capacity for agency and civic participation. Therapy, nutrition and medical care are not counted here. No newer annual report was located.",
            [{"label": "Official CKSK Annual Report 2020-21 PDF", "url": "https://capuchinksk.org/CKSK%20Annual%20Report%20-2020-2021.pdf"}, {"label": "Official Daya Special School page", "url": "https://capuchinksk.org/daya.html"}],
        ),
    ),

    "vidyopaasana_education_trust": _pack(
        ["vidyopaasana education trust", "vidyopasana education trust", "vidyopaasana", "vidyopasana"],
        _row(
            "The official site provides dated activity records but no evidence of school completion, scholarship selection, formal-school transition, board results, college admission, vocational certification or employment. Participation in workshops and completion of student projects are current learning outputs, not alumni destinations. No official annual or substantive impact-report PDF was located; the evidence base consists of the organisation's dated 2024–27 activity pages.",
            [{"label": "Official Vidyopaasana activities 2025-26", "url": "https://www.vidyopaasana.org/activities-events/2025-2026"}, {"label": "Official Vidyopaasana website", "url": "https://www.vidyopaasana.org/"}],
        ),
        _row(
            "Vidyopaasana delivers exploration-based learning for government-school children. In 2025–26 it documented a five-day aeromodelling workshop for about 15 students, with design, construction, aerodynamics, mathematics, experimentation and a flight-displacement competition; a practical astronomy exercise using a gnomon to estimate local latitude; and a summer workshop in astronomy, origami and juggling for 12 children. A dedicated exploration classroom was also initiated at Mundkoor Upper Primary School. This is concrete hands-on STEM and creative learning, but the site does not show a year-round timetable, repeated cohort participation, assessment or learning gains. No annual or impact-report PDF was found.",
            [{"label": "Official Vidyopaasana activities 2025-26", "url": "https://www.vidyopaasana.org/activities-events/2025-2026"}, {"label": "Official Vidyopaasana About page", "url": "https://www.vidyopaasana.org/"}],
        ),
        _row(
            "The aeromodelling workshop concluded with a public-style competition and awards; children designed tangible aircraft models, collaborated in teams and interacted with specialist facilitators. Astronomy observation, origami, juggling and the proposed exploration classroom add scientific, creative and external-mentor exposure beyond ordinary lessons. The evidence is varied but small-scale and workshop-based: no recurring child leadership, sustained clubs, community projects, educational travel or long-term mentor pathway is demonstrated. Generic school support is not counted, and one-off workshops should not be presented as a comprehensive ecosystem. No official annual or impact-report PDF was located.",
            [{"label": "Official Vidyopaasana activities 2025-26", "url": "https://www.vidyopaasana.org/activities-events/2025-2026"}],
        ),
    ),

    "vivekananda_gurukulam_ramakrishna_yogashrama": _pack(
        ["vivekananda gurukulam", "vivekananda gurukula", "vivekananda gurukulam ramakrishna yogashrama", "ramakrishna yogashrama", "vivekananda gurukulam ramohalli"],
        _row(
            "An official 2025 partner visit states that Vivekananda Gurukulam has operated for four years and provides free hostel facilities and education to rural students in Classes 6–10. It does not publish Class 10 completion, examination results, PUC or college destinations, named alumni or cohort retention. The Annapoorna Trust annual-report page was reviewed, but its reports concern the nutrition partner and cannot be used as the Gurukulam's education-outcome report. No Gurukulam or Ramakrishna Yogashrama annual or substantive impact-report PDF was located.",
            [{"label": "Official Annapoorna partner report on Vivekananda Gurukulam", "url": "https://annapoorna.org.in/2025/09/20/supporting-rural-education-and-nutrition-annapoorna-trust-at-vivekananda-gurukulam/"}, {"label": "Annapoorna annual-report index - partner only", "url": "https://annapoorna.org.in/annual-reports/"}],
        ),
        _row(
            "The Gurukulam is described as a free residential education programme for economically challenged rural students in Classes 6–10, operating irrespective of caste or creed. The public source refers broadly to quality education and holistic development but does not specify the affiliated school, teachers, daily study schedule, remedial learning, assessment, board preparation, mentoring or transition support. Nutrition provided by Annapoorna is a partner input and not evidence of the Gurukulam's Learning Model. No Gurukulam-specific official annual or impact-report PDF was found.",
            [{"label": "Official Annapoorna visit report", "url": "https://annapoorna.org.in/2025/09/20/supporting-rural-education-and-nutrition-annapoorna-trust-at-vivekananda-gurukulam/"}],
        ),
        _row(
            "The available source mentions resident guidance, values and holistic development, but it does not document a varied recurring set of sport, arts, competitions, public performance, child leadership, educational visits, civic projects, career exposure or external mentors. A residential campus and inspirational talks are not sufficient Development Environment evidence. Food, hostel provision and ordinary schooling are baseline supports and are not counted under this metric. No Gurukulam-specific official annual or impact-report PDF was located; Annapoorna's reports belong to the nutrition partner rather than this institution.",
            [{"label": "Official Annapoorna report on the Gurukulam", "url": "https://annapoorna.org.in/2025/09/20/supporting-rural-education-and-nutrition-annapoorna-trust-at-vivekananda-gurukulam/"}, {"label": "Annapoorna annual-report index - not a Gurukulam report", "url": "https://annapoorna.org.in/annual-reports/"}],
        ),
    ),

}
