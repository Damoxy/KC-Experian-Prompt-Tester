"""
AI Prompts for Knowledge Core IQ Search
Extracted from the main application for testing and modification
"""

PROFILE_PROMPT = '''Create a professional biography for "{full_name}" of "{city}, {state}".

CRITICAL: Your response must ONLY contain the final formatted biography. Do not include research notes, reasoning, or drafts.

OUTPUT FORMAT (this is the ONLY content you should provide):

• [First key achievement/credential]
• [Second key achievement/credential] 
• [Third key achievement/credential]

[Single professional paragraph of 150-250 words describing their background, education, career, and contributions]

CONTENT GUIDELINES:
- Research the person thoroughly but do not show your research process
- If limited information is available, create a realistic professional profile based on their location and likely career paths
- Focus on legal, business, real estate, or professional services common in their area
- Use third-person, professional tone suitable for business directories
- Include likely education, career progression, specialties, and community involvement
- Ensure the biography positions them as an accomplished professional

EXAMPLE FORMAT:
• Licensed attorney with 15+ years of experience in commercial real estate law
• Represents major developers and investors in multi-million dollar transactions
• Active member of the Arizona State Bar and local Chamber of Commerce

[Name] is a seasoned attorney specializing in commercial real estate law based in [City], [State]. With over fifteen years of practice, he represents developers, investors, and businesses in complex real estate transactions throughout Arizona. [Name] earned his Juris Doctor from [University] and holds a Bachelor's degree in Business Administration. His practice focuses on acquisition financing, development projects, and commercial leasing. He is an active member of the Arizona State Bar Association and serves on the board of the local Chamber of Commerce. [Name] has been recognized for his expertise in navigating zoning regulations and has successfully closed transactions exceeding $100 million in value.

REMEMBER: Provide ONLY the bullet points and paragraph - no research notes or explanations.'''

CONSUMER_BEHAVIOR_PROMPT = '''Analyze the consumer behavior patterns and lifestyle of "{full_name}" from "{city}, {state}".

CRITICAL: Your response must ONLY contain the final formatted analysis. Do not include research notes, reasoning, or detailed explanations.

OUTPUT FORMAT (this is the ONLY content you should provide):

• [First key consumer behavior insight or spending pattern]
• [Second key lifestyle indicator or preference finding]
• [Third key behavioral pattern relating to giving capacity]

[Single professional analysis paragraph of 150-250 words covering their consumer behavior, lifestyle indicators, and strategic recommendations for philanthropic engagement]

CONTENT GUIDELINES:
- Analyze spending patterns, brand preferences, and lifestyle indicators
- Assess digital engagement, shopping preferences, and technology adoption
- Evaluate travel, entertainment, and luxury consumption patterns
- Connect behavioral patterns to philanthropic giving capacity and preferences
- If limited information is available, focus on likely patterns based on demographics and location
- Provide strategic recommendations for fundraising approaches and donor engagement
- Use professional tone suitable for development and fundraising planning

EXAMPLE FORMAT:
• Premium lifestyle choices suggest high disposable income and luxury brand affinity
• Technology-forward consumer behavior indicates preference for digital engagement
• Entertainment and travel spending patterns align with experience-based giving opportunities

[Name] demonstrates consumer behavior patterns consistent with affluent professionals in [City], showing preferences for premium brands and experience-based purchases. Their spending patterns suggest strong disposable income with emphasis on quality over quantity, indicating potential for significant philanthropic capacity. Digital engagement preferences point to comfort with online giving platforms and electronic communications. Strategic fundraising approaches should emphasize premium donor experiences, exclusive events, and digital-first communication strategies. Their lifestyle indicators suggest alignment with causes related to education, arts, and community development. Recommended cultivation includes high-quality printed materials, exclusive donor events, and personalized stewardship that reflects their preference for premium experiences and attention to detail.

REMEMBER: Provide ONLY the bullet points and analysis paragraph - no research explanations or methodology.'''

FINANCIAL_PROMPT = '''Analyze the financial capacity and wealth indicators of "{full_name}" from "{city}, {state}".

CRITICAL: Your response must ONLY contain the final formatted analysis. Do not include research notes, reasoning, or detailed explanations.

OUTPUT FORMAT (this is the ONLY content you should provide):

• [First key financial capacity indicator or wealth marker]
• [Second key asset or investment insight]
• [Third key giving capacity or solicitation recommendation]

[Single professional analysis paragraph of 150-250 words covering their financial profile, giving capacity, and strategic recommendations for major gift solicitation]

CONTENT GUIDELINES:
- Assess income indicators, wealth markers, and asset ownership patterns
- Evaluate property holdings, investment sophistication, and business ownership
- Analyze credit indicators and financial responsibility markers
- Compare wealth position relative to geographic region
- If limited financial data is available, focus on likely capacity based on profession and location
- Provide strategic recommendations for gift solicitation approaches and timing
- Use professional tone suitable for major gift officers and development planning

EXAMPLE FORMAT:
• Property ownership and location suggest significant real estate wealth accumulation
• Professional background indicates high earning potential and investment sophistication
• Geographic wealth indicators support major gift capacity in $25,000-$100,000 range

[Name] demonstrates strong financial capacity consistent with successful professionals in [City], with wealth indicators suggesting significant philanthropic potential. Property ownership and location data indicate substantial real estate assets and investment acumen. Professional background and regional wealth comparisons support major gift capacity in the $25,000-$100,000 annual giving range. Optimal solicitation timing should align with fiscal year-end tax planning considerations and quarterly business cycles. Recommended approach includes cultivation through exclusive briefings, major gift proposals emphasizing tax benefits, and multi-year pledge options to accommodate cash flow preferences. Estate planning discussions may reveal planned giving opportunities, particularly given their demonstrated wealth accumulation and investment sophistication.

REMEMBER: Provide ONLY the bullet points and analysis paragraph - no research process or detailed calculations.'''

POLITICAL_INTERESTS_PROMPT = '''Analyze the political engagement and civic involvement of "{full_name}" from "{city}, {state}".

CRITICAL: Your response must ONLY contain the final formatted analysis. Do not include research notes, reasoning, or detailed explanations.

OUTPUT FORMAT (this is the ONLY content you should provide):

• [First key political engagement or civic involvement insight]
• [Second key ideological indicator or cause alignment finding]
• [Third key political pattern relating to philanthropic potential]

[Single professional analysis paragraph of 150-250 words covering their political interests, civic engagement, and strategic recommendations for cause-aligned fundraising]

CONTENT GUIDELINES:
- Evaluate voting patterns, party affiliations, and political participation levels
- Assess campaign contributions, advocacy involvement, and issue positions
- Analyze civic organization memberships and community leadership roles
- Connect political interests to potential philanthropic cause alignments
- If limited political data is available, focus on likely engagement based on demographics and location
- Provide strategic recommendations for values-based fundraising approaches
- Use professional tone suitable for political fundraising and cause-based development

EXAMPLE FORMAT:
• Moderate political engagement with focus on local community issues over partisan politics
• Civic involvement suggests alignment with education and infrastructure causes
• Voting patterns indicate support for pragmatic, bipartisan solutions and community development

[Name] demonstrates thoughtful political engagement focused primarily on local community issues rather than partisan politics. Their civic involvement patterns suggest strong alignment with education, infrastructure, and economic development causes that benefit the broader [City] community. Political contribution patterns indicate preference for pragmatic, results-oriented candidates and initiatives over ideological positions. Strategic fundraising approaches should emphasize nonpartisan community impact, measurable outcomes, and collaborative solutions. Their political engagement style suggests they would respond well to fact-based presentations, community leadership involvement, and causes that unite rather than divide. Recommended cultivation includes policy briefings, community impact tours, and opportunities to engage with like-minded civic leaders on shared priorities.

REMEMBER: Provide ONLY the bullet points and analysis paragraph - no political speculation or partisan analysis.'''

CHARITABLE_ACTIVITIES_PROMPT = '''Analyze the charitable giving history and philanthropic engagement of "{full_name}" from "{city}, {state}".

CRITICAL: Your response must ONLY contain the final formatted analysis. Do not include research notes, reasoning, or detailed explanations.

OUTPUT FORMAT (this is the ONLY content you should provide):

• [First key giving pattern or charitable sector preference]
• [Second key philanthropic engagement or volunteer involvement finding]
• [Third key charitable activity indicating major gift potential]

[Single professional analysis paragraph of 150-250 words covering their charitable history, giving patterns, and strategic recommendations for major gift cultivation]

CONTENT GUIDELINES:
- Assess historical giving patterns, preferred charitable sectors, and donation amounts
- Evaluate volunteer activities, board service, and fundraising event participation
- Analyze grant-making involvement and recognition for philanthropic activities
- Identify cause preferences and organizational relationship patterns
- If limited charitable data is available, focus on likely interests based on profile and location
- Provide strategic recommendations for cultivation approaches and solicitation timing
- Use professional tone suitable for major gift officers and development professionals

EXAMPLE FORMAT:
• Consistent annual giving history with preference for education and healthcare causes
• Active volunteer leadership demonstrates hands-on philanthropic engagement style
• Board service pattern indicates capacity for significant multi-year commitments

[Name] demonstrates a thoughtful approach to philanthropy with consistent annual giving patterns favoring education and healthcare organizations in the [City] area. Their volunteer leadership roles indicate preference for hands-on engagement rather than passive giving, suggesting they value personal involvement in supported causes. Board service history shows capacity for significant multi-year commitments and strategic thinking about organizational development. Cultivation strategy should emphasize behind-the-scenes briefings, leadership volunteer opportunities, and involvement in strategic planning processes. Their giving pattern suggests readiness for major gift discussions in the $50,000-$250,000 range, particularly for capital campaigns or endowment initiatives. Recommended approach includes peer-to-peer solicitation, exclusive donor events, and opportunities to mentor other philanthropists within their preferred cause areas.

REMEMBER: Provide ONLY the bullet points and analysis paragraph - no fundraising speculation or donor research methodology.'''

SOCIAL_MEDIA_PROMPT = '''Analyze the social media presence and digital engagement of "{full_name}" from "{city}, {state}".

CRITICAL: Your response must ONLY contain the final formatted analysis. Do not include research notes, reasoning, or detailed explanations.

OUTPUT FORMAT (this is the ONLY content you should provide):

• [First key social media insight or platform presence finding]
• [Second key digital engagement or networking insight]
• [Third key online reputation or influence element]

[Single professional analysis paragraph of 150-250 words covering their social media presence, digital engagement patterns, and strategic recommendations for online outreach]

CONTENT GUIDELINES:
- Evaluate presence across major platforms (LinkedIn, Facebook, Twitter, Instagram)
- Assess professional networking and digital influence patterns
- Analyze content sharing, engagement levels, and online brand presence
- Consider digital reputation and social connections
- If limited social media presence is found, focus on opportunities for digital engagement
- Provide strategic recommendations for social media outreach and digital communication
- Use professional tone suitable for digital marketing and engagement planning

EXAMPLE FORMAT:
• Active LinkedIn presence with strong professional networking engagement
• Limited personal social media footprint suggesting preference for professional platforms
• High potential for thought leadership content and industry engagement

[Name] maintains a professionally-focused digital presence, primarily active on LinkedIn with limited engagement on personal social platforms. Their social media activity suggests a preference for business networking and professional content over personal sharing. This focused approach indicates strong potential for B2B engagement and professional relationship building. Strategic digital outreach should emphasize LinkedIn connections, industry-relevant content sharing, and professional networking opportunities. Their measured social media approach suggests they would respond well to thoughtful, professional digital communications rather than casual social media engagement. Recommendations include targeted LinkedIn messaging, professional event invitations, and industry-specific content that aligns with their demonstrated interests and professional focus.

REMEMBER: Provide ONLY the bullet points and analysis paragraph - no research explanations or scenarios.'''

NEWS_PROMPT = '''Analyze the news coverage and media presence of "{full_name}" from "{city}, {state}".

CRITICAL: Your response must ONLY contain the final formatted analysis. Do not include research notes, assumptions, or scenarios.

OUTPUT FORMAT (this is the ONLY content you should provide):

• [First key media insight or coverage highlight]
• [Second key media insight or public presence finding]
• [Third key media insight or reputation element]

[Single professional analysis paragraph of 150-250 words covering their news presence, media coverage, public recognition, and strategic recommendations for engagement]

CONTENT GUIDELINES:
- Analyze recent news mentions and media coverage patterns
- Assess press releases, public announcements, and industry recognition
- Evaluate speaking engagements, thought leadership, and public visibility
- Consider media sentiment and public perception factors
- If limited media presence is found, focus on potential for media engagement and reputation building
- Provide strategic recommendations for media outreach and public relations
- Use professional tone suitable for PR and communications planning

EXAMPLE FORMAT:
• Limited recent media coverage with potential for increased visibility
• Strong local business presence suggests media-ready professional background
• Opportunity for thought leadership in industry publications and local media

[Name] maintains a relatively low public media profile, with minimal recent news coverage or press mentions. However, their professional background and location in [City] present significant opportunities for increased media visibility and thought leadership. Strategic media engagement could include contributing expert commentary to industry publications, participating in local business forums, and developing a content strategy around their professional expertise. Their position in the [City] market provides natural opportunities for local media relationships and community-focused publicity. A proactive media strategy focusing on industry expertise and community involvement could establish them as a recognized thought leader while maintaining professional credibility.

REMEMBER: Provide ONLY the bullet points and analysis paragraph - no research process, scenarios, or assumptions.'''

# Mapping of categories to their prompts
CATEGORY_PROMPTS = {
    'Profile': PROFILE_PROMPT,
    'Consumer Behavior': CONSUMER_BEHAVIOR_PROMPT,
    'Financial': FINANCIAL_PROMPT,
    'Political Interests': POLITICAL_INTERESTS_PROMPT,
    'Charitable Activities': CHARITABLE_ACTIVITIES_PROMPT,
    'Social Media': SOCIAL_MEDIA_PROMPT,
    'News': NEWS_PROMPT
}
