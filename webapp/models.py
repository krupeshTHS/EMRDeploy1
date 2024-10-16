from django.db import models
from datetime import date

class Record(models.Model):
    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    ssn = models.CharField(max_length=125, default= '')

    dob = models.CharField(max_length=125, default= '')

    facility_name = models.CharField(max_length=125, default= '')

    sex = models.CharField(max_length=6, default= '')

    status = models.CharField(max_length=10, default='')

    primary_insurance_name =models.CharField(max_length=100, default='')

    primary_insurance = models.CharField(max_length=100, default='')

    secondary_insurance = models.CharField(max_length=100, default ='')

    eligibility_status = models.CharField(max_length=100 , default='')

    copay = models.CharField(max_length=4, default='')

    ded = models.CharField(max_length=4, default='')

    coinsurance = models.CharField(max_length=4, default='')

    referred_by =models.CharField(max_length=100, default='')

    eligibility_comments = models.CharField(max_length=500, default='')

    eligibility_rundate = models.CharField(max_length=500, default='')

    talk_therapy_doc_name = models.CharField(max_length=100, default='')

    med_management_doc_name = models.CharField(max_length=100, default='')

    assign_date = models.CharField(max_length=100, default='')

    additional_notes = models.CharField(max_length=100, default= '')

    responsible_party_name = models.CharField(max_length=100, default ='')

    responsible_party_relationaship = models.CharField(max_length=100, default ='')

    responsible_party_Number = models.CharField(max_length=100, default ='')

    responsible_party_Email = models.CharField(max_length=100, default ='')

    pharmacy_information = models.CharField(max_length=100, default ='')

    diagnosis_information = models.TextField(max_length=100, default ='')



    def __str__(self):

        return self.first_name + "   " + self.last_name
    
class ChildForm(models.Model):
    LETTER_HEAD_CHOICES =(
            ('1','CHILD NET'),
            ('2','DYNAMIC HEADER'),
        )
    
    EVALUATION_DONE_VIA_CHOICES = (('1', 'Evaluation done via Phone'),
                                   ('2', 'Evaluation done via Video Conference'),
                                   )
    
    POSCHOICES = (('1', 'TELEHEALTH'),
                  ('2', 'HOME'),
                  ('3', 'OFFICE'),
                  )
    letterhead = models.CharField(max_length=1000, choices= LETTER_HEAD_CHOICES)

    evaluationDoneVia = models.CharField(max_length=1000, choices= EVALUATION_DONE_VIA_CHOICES)

    dateOfEvaluation = models.DateField()

    dob = models.CharField(max_length=1250, default= '')

    age = models.CharField(max_length=1000)

    patientName = models.CharField(max_length=1000, default ='', blank=True)

    sex = models.CharField(max_length =1000)

    evaluatedBy = models.CharField(max_length =1000, default ='')

    time_in = models.CharField(max_length=1000)

    time_out =models.CharField(max_length=1000)

    parent = models.CharField(max_length=1000)

    maratialStatus = models.CharField(max_length=1000)

    custody = models.CharField(max_length=1000)

    pos = models.CharField(max_length=1000, choices= POSCHOICES)

    schoolname = models.CharField(max_length=1000)

    grade = models.CharField(max_length=1000)

    primarycarephysicianDoc = models.CharField(max_length=1000)

    primarycarephysicianDocTelephone = models.CharField(max_length=1000)

    therapist = models.CharField(max_length=1000)

    thrapistTelephone = models.CharField(max_length=1000)

    problemList = models.TextField(max_length=1000)

    historyofPresentingProblem = models.TextField(max_length=5000)

    psychistorydate1 =models.DateField()

    psychistorydate2 = models.DateField()

    psychistorydate3 = models.DateField()

    provider = models.CharField(max_length=1000)

    provider2 = models.CharField(max_length=1000)

    provider3= models.CharField(max_length=1000)

    type = models.CharField(max_length=1000)

    type2 = models.CharField(max_length=1000)

    type3 = models.CharField(max_length=1000)

    outcome = models.CharField(max_length=1000)

    outcome2 = models.CharField(max_length=1000)

    outcome3 = models.CharField(max_length=1000)

    # Past Medical/surgical history
    allergies =models.CharField(max_length=1000)

    immunizations = models.CharField(max_length=1000)

    lastphysicalexamination = models.CharField(max_length=1000)

    historyofheadInjury = models.CharField(max_length=1000)

    surgery =models.CharField(max_length=1000)

    seizure = models.CharField(max_length=1000)

    chronicillness = models.CharField(max_length=1000)

    currentMedication =models.TextField(max_length=1000)

    familyHistory =models.TextField(max_length=1000)

    #Developmental history

    maternalHealth = models.CharField(max_length=1000)

    prenatalPerinalPostnatalHealth = models.CharField(max_length=1000)

    earlyDevelopment =models.CharField(max_length=1000)

    speechLanguage =models.CharField(max_length=1000)

    physicalEmotionalSexualHistory = models.TextField(max_length=5000)

    soicalHistory = models.TextField(max_length=5000)

    #School History
    earlySchoolingAdjustment = models.CharField(max_length=1000)

    separationAnxiety = models.CharField(max_length=1000)

    Socialization = models.CharField(max_length=1000)

    transfer = models.CharField(max_length=1000)

    cognitiveandAcademicFunctioning = models.CharField(max_length=1000)

    behaviorProblems = models.CharField(max_length=1000)

    #Mental Status Examination
    WELLGROOMEDLEVELSChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    UNKEMPTLEVELSCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    DISHEVELEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    eyeCotactAverageLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    eyecontactAvoidantLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    eyecontactIntenseLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    buildAverageLevelChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    buildThinLevelChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    buildOverweightLevelsChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    ACTIVITYAVERAGECHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    ACTIVITYAGITATEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    SLOWEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    #Appearance
    appearanceWellgrommed = models.BooleanField(default=False)
    
    appearanceWellgroomedLevels= models.CharField(max_length=100, choices=WELLGROOMEDLEVELSChoices)
    
    appearanceUnkempt = models.BooleanField(default=False)

    appearanceUnkemptLevels = models.CharField(max_length=100, choices=UNKEMPTLEVELSCHOICES)

    appearanceDisheveled = models.BooleanField(default=False)

    appearanceDisheveledLevels= models.CharField(max_length=100, choices=DISHEVELEDCHOICES)

    #Eye Contact
    eyeCotactAverage = models.BooleanField(default=False)
    
    eyeCotactAverageLevels= models.CharField(max_length=100, choices=eyeCotactAverageLevelsChoices)
    
    eyecontactAvoidant = models.BooleanField(default=False)

    eyecontactAvoidantLevels = models.CharField(max_length=100, choices=eyecontactAvoidantLevelsChoices)

    eyecontactIntense = models.BooleanField(default=False)

    eyecontactIntenseLevels= models.CharField(max_length=100, choices=eyecontactIntenseLevelsChoices)

    
    
    #build
    buildAverage = models.BooleanField(default=False)
    
    buildAverageLevels= models.CharField(max_length=100, choices=buildAverageLevelChoice)
    
    buildThin = models.BooleanField(default=False)

    eyecontacbuildThinLevels = models.CharField(max_length=100, choices=buildThinLevelChoice)

    buildOverweight = models.BooleanField(default=False)

    buildOverweightLevels= models.CharField(max_length=100, choices=buildOverweightLevelsChoice)

    
    #Activity
    activityAverage = models.BooleanField(default=False)
    
    activityAverageLevels= models.CharField(max_length=100, choices=ACTIVITYAVERAGECHOICES)
    
    activityAgitated = models.BooleanField(default=False)

    activityAgitatedLevels = models.CharField(max_length=100, choices=ACTIVITYAGITATEDCHOICES)

    activitySlowed = models.BooleanField(default=False)

    activitySlowedLevels= models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Demeanor

    demeanorAverage = models.BooleanField(default=False)

    demeanorAverageLevels =models.CharField(max_length=100, choices=SLOWEDCHOICES)

    demeanorHostile = models.BooleanField(default=False)

    demeanorHostileLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorMistrustful = models.BooleanField(default=False)

    demeanorMistrustfulLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorWithdrawn = models.BooleanField(default=False)

    demeanorWithdrawnLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorPreoccupied = models.BooleanField(default=False)

    demeanorPreoccupiedLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorDemanding = models.BooleanField(default=False)

    demeanorDemandingLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)


    #Speech

    speechClear = models.BooleanField(default=False)

    speechClearLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechSlurred = models.BooleanField(default=False)

    speechSlurredLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechRapid = models.BooleanField(default=False)

    speechRapidLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechPressured = models.BooleanField(default=False)

    speechPressuredLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Delusions

    delusionsNoneReported = models.BooleanField(default= False)

    delusionsgrandiose = models.BooleanField(default=False)

    delusionsgrandioseLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionspersecutory = models.BooleanField(default= False)

    delusionspersecutoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionssomatic =models.BooleanField(default=False)

    delusionssomaticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsbizarre =models.BooleanField(default=False)

    delusionsbizarreLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsnihilistic = models.BooleanField(default=False)

    delusionsnihilisticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsreligious = models.BooleanField(default=False)

    delusionsreligiouslevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Self Abuse

    selfAbuseNonreported = models.BooleanField(default=False)

    selfAbuseSelfMutilation = models.BooleanField(default=False)

    selfAbuseSelfMutilationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbuseSucidal = models.BooleanField(default=False)

    selfAbuseSucidalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbuseIntent = models.BooleanField(default=False)

    selfAbuseIntentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbusePlan = models.BooleanField(default=False)

    selfAbusePlanLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #other

    otherNoneReported = models.BooleanField(default= False)

    otherAutistic = models.BooleanField(default =False)

    otherAutisticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherObsessional =models.BooleanField(default=False)

    otherObsessionalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPhobic = models.BooleanField(default=False)

    otherPhobicLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherGuilty = models.BooleanField(default=False)

    otherGuiltyLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherIdeasOfreference = models.BooleanField(default= False)

    otherIdeasOfreferenceLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES) 

    otherPreoccupied = models.BooleanField(default=False)

    otherPreoccupiedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherGuraded = models.BooleanField(default=False)

    otherGuradedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherOption = models.BooleanField(default=False)

    otherOptionText = models.CharField(max_length=1000)

    #Aggressive

    aggressiveNoneReported = models.BooleanField(default=False)

    aggressiveHomicidal = models.BooleanField(default=False)

    aggressiveHomicidalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    aggresiveIntent = models.BooleanField(default=False)

    aggresiveIntentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    aggressivePlan = models.BooleanField(default=False)

    aggressivePlanLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    
    
    #Perception/Hallucinations

    hallucinationsNoneReported = models.BooleanField(default= False)

    hallucinationsAuditory = models.BooleanField(default=False)

    hallucinationsAuditoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsVisual = models.BooleanField(default= False)

    hallucinationsVisualLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsOlfactory = models.BooleanField(default=False)

    hallucinationsOlfactoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsGustatory = models.BooleanField(default = False)

    hallucinationsGustatoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsTactile = models.BooleanField(default= False)

    hallucinationsTactileLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Other/Perception

    otherPerceptionNonreported = models.BooleanField(default= False)

    otherPerceptionIllusions = models.BooleanField(default =False)

    otherPerceptionIllusionsLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPerceptionDepersonalization = models.BooleanField(default=False)

    otherPerceptionDepersonalizationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPerceptionDerealization = models.BooleanField(default=False)

    otherPerceptionDerealizationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Thought Process

    thoughtProcessLogical = models.BooleanField(default= False)
    
    thoughtProcessLogicalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessCircumstantial = models.BooleanField(default = False)

    thoughtProcessCircumstantialLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessTangential = models.BooleanField(default= False)

    thoughtProcessTangentialLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessLoose = models.BooleanField(default=False)

    thoughtProcessLooseLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessRacing = models.BooleanField(default= False)

    thoughtProcessRacingLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessIncoherent = models.BooleanField(default= False)

    thoughtProcessIncoherentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessConcrete = models.BooleanField(default= False)

    thoughtProcessConcreteLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessBlocked = models.BooleanField(default= False)

    thoughtProcessBlockedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessFlightOfIdeas = models.BooleanField(default= False)

    thoughtProcessFlightOfIdeasLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #mood

    moodEuthymic = models.BooleanField(default= False)

    moodEuthymicLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodDepressed = models.BooleanField(default= False)

    moodDepressedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodAnxious = models.BooleanField(default= False)

    moodAnxiousLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodAngry = models.BooleanField(default= False)

    moodAngryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodEuphoric = models.BooleanField(default= False)
    
    moodEuphoricLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodIrritable = models.BooleanField(default= False)

    moodIrritableLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Affect

    affectFull = models.BooleanField(default= False)

    affectFullLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectConstricted = models.BooleanField(default= False)

    affectConstrictedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectFlat = models.BooleanField(default= False)

    affectFlatLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectInappropriate = models.BooleanField(default= False)

    affectInappropriateLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectLabile = models.BooleanField(default= False)

    affectLabileLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Behavior

    behaviorCooperative = models.BooleanField(default= False)

    behaviorCooperativelevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorResistant = models.BooleanField(default= False)

    behaviorResistantLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAgitated = models.BooleanField(default= False)

    behaviorAgitatedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorImpulsive = models.BooleanField(default= False)

    behaviorImpulsiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorOverSedated = models.BooleanField(default= False)

    behaviorOverSedatedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    
    #
    behaviorAssaultive = models.BooleanField(default= False)

    behaviorAssaultiveLevels =models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAggresive = models.BooleanField(default= False)

    behaviorAggresiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorHyperactive = models.BooleanField(default= False)

    behaviorHyperactiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorRestless = models.BooleanField(default= False)

    behaviorRestlessLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorLossOfInterest = models.BooleanField(default= False)

    behaviorLossOfInterestLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    #
    behaviorAnhedonia = models.BooleanField(default= False)
    
    behaviorAnhedoniaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAkasthisia = models.BooleanField(default= False)

    behaviorAkasthisiaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorWithdrawn = models.BooleanField(default= False)

    behaviorWithdrawnLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorDystonia = models.BooleanField(default= False)

    behaviorDystoniaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorTardive = models.BooleanField(default= False)

    behaviorTardiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorDyskinesia = models.BooleanField(default= False)

    behaviorDyskinesiaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Cognition

    impairmentofNonReported = models.BooleanField(default= False)

    impairmentofOrientation = models.BooleanField(default= False)

    impairmentofOrientationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofMemory = models.BooleanField(default= False)

    impairmentofMemoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofAttentionConcentration = models.BooleanField(default= False)

    impairmentofAttentionConcentrationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofAbilityToAbstract = models.BooleanField(default= False)

    impairmentofAbilityToAbstractLevels = models.CharField(max_length=100, choices= SLOWEDCHOICES)

    #Intelligence

    IntelligenceMR = models.BooleanField(default= False)

    IntelligenceMRLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceBorderline = models.BooleanField(default= False)

    IntelligenceBorderlineLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceAverage = models.BooleanField(default= False)

    IntelligenceAverageLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceAboveAverage = models.BooleanField(default= False)

    IntelligenceAboveAverageLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Insight judgement 

    InsightjudgementNA = models.BooleanField(default= False)

    Insightjudgement = models.CharField(max_length=1000, default= '')


    unableToAssessAppearanceAndMotorActivityViaPhone = models.BooleanField(default= False)

    # ICD codes
     
    ICDCODES =(
        ('1','F31.73- Bipolar disorder, in partial remission, most recent episode manic'),
        ('2', 'F05	Delirium due to another medical condition'),
        ('3', 'F05	Delirium due to multiple etiologies'),
        ('4', 'F06.0	Psychotic disorder due to another medical condition, With hallucinations'),
        ('5', 'F06.1	Catatonia associated with another mental disorder (catatonia specifier)'),
        ('6', 'F06.1	Catatonic disorder due to another medical condition'),
        ('7','F07'),)
    
    #TODo

    icdcode = models.CharField(max_length=1000, choices=SLOWEDCHOICES)
    #DX

    dx = models.CharField(max_length=1000, default ='')

    dx1 = models.CharField(max_length=1000, default='')

    dx2 = models.CharField(max_length=1000, default='')

    dx3 = models.CharField(max_length=1000, default='')

    #CPT Code

    CPTCODES = (
        ('1', '99201 - Office_OP New Pat Initial minimum Cmplexity 10 mins'),
        ('2', '99202 - Office_OP New Pat Initial Low Compelexity 20 mins'),
        ('3', '99203 - Office_OP New Pat Initial Moderate Compelexity 30 mins'),
        ('4', '99204 - Office_OP New Pat Initial Comprehensive Compelexity 45 mins'),
        ('5', '99205 - Office_OP New Pat Initial High Compelexity 60 mins'),
        ('6', '99211 - Office_Op Est Pat Follow-Up Minimum Complex 5 mins'),
        ('7', '99212 - Office_Op Est Pat Follow-Up Low Complex 5 mins'),
        ('8', '99213 - Office _OP Est Pat Follow-Up Moderate COmplex 15 mins'),
        ('9', '99214 - Office_OP Est Follow Up Comprehensive Complex 25 mins'),
        ('10','99215 - Office_OP Est Pat Follow-Up High Complex 40 mins'),
        ('11', '99304 - Nursing New Pat Initial Low Complexity 25 mins'),
        ('12', '99305 - Nursing New Pat Initial Moderate Complexity 35 mins'),
        ('13', '99306 - Nursing New Pat Initial High Complexity 45 mins'),
        ('14', '99307 - Nursing Est pat Follow-Up Minimum Complex 10 mins'),
        ('15', '99308 - Nursing Est Pat Fllow-Up Low Complex 15 mins'),
        ('16', '99309 - Nursing Est Pat Follow-Up Moderate Complex 25 mins'),
        ('17', '99310 - Nursing Est Pat Follow-Up High Complex 35 mins'),
        ('18', '99318 - Nursing Est Pat Annual Assessment 60 mins'),
        ('19', '99341 - ALF New Pat New Patient Minimum Complex 15 mins'),
        ('20', '99342 - ALF New Pat New Patient Low Complex 30 mins'), 
        ('21', '99344 - ALF New Pat New Patint Moderate Complex 60 mins'),
        ('22', '99345 - ALF New Pat New Patent Comprehensive Comp. 75 mins'),
        ('23', '99417 - ALF New Pat add on for additional time past High 15 mins'),
        ('24', '99347 - ALF Est Pat Est Pt Min complex 20 mins'),
        ('25', '99348 - ALF Est Pat Est Pt Low COmplex 30 mins'),
        ('26', '99349 - ALF Est Pat Est Pt Moderate Complex 40 mins'),
        ('27', '99350 - ALf Est Pat Est Pt High Complex 60 mins'),
    )

    MODIFIERS = (
        ('1', 'GW - HOSPICE'),
        ('2', '95 - TELEHEALTH'),
    )
    cptcode1 = models.CharField(max_length=1000, choices=CPTCODES)

    cptcodeother1 = models.CharField(max_length= 1000, default = '')

    unit1 = models.CharField(max_length= 100, default= '')

    modifiers1 =models.CharField(max_length=100, choices=MODIFIERS)

    modifiers2 = models.CharField(max_length=100, choices=MODIFIERS)

    modifiersOther1 = models.CharField(max_length=1000, default ='')

    modifiersOther2 = models.CharField(max_length=1000, default ='')

    cptcode2 =  models.CharField(max_length=1000, choices=CPTCODES)

    cptcodeOther2 = models.CharField(max_length=1000, default='')

    unit2 = models.CharField(max_length=100, default = '')

    modefiers3 = models.CharField(max_length=100, choices=MODIFIERS)

    modefiers4 = models.CharField(max_length=100, choices=MODIFIERS)

    modefiersOther3 = models.CharField(max_length=1000, default ='')

    modefiersOther4 = models.CharField(max_length=1000, default ='')


    commentToBillers = models.TextField(max_length=10000, default='')

    commentMedical = models.TextField(max_length=10000, default='')

    commentStressors = models.TextField(max_length=10000, default='')

    commentImpressionTreatmentPlan = models.TextField(max_length=10000, default= '')

    dateatheendOfForm = models.DateField(default= date.today)
    
    def __str__(self):

        return self.patientName


    #brief Note Model
class BriefNote(models.Model):

    LETTER_HEAD_CHOICES =(
            ('1','CHILD NET'),
            ('2','DYNAMIC HEADER'),
        )

    letterhead = models.CharField(max_length=1000, choices= LETTER_HEAD_CHOICES)

    time_in = models.TimeField()

    time_out = models.TimeField()

    dateOfAppointment = models.DateField(default=date.today)

    natureofContactOutForAppointment= models.BooleanField(default =False)

    natureofContactRefused1stAttempt = models.BooleanField(default =False)

    natureofContactrefused2ndAttempt = models.BooleanField(default= False)

    natureofContactrefused3rdAttempt = models.BooleanField(default = False)

    natureofContactInthHospital = models.BooleanField(default= False)

    natureofContactInRehab = models.BooleanField(default =False)

    natureofContactQuickDeEscalation = models.BooleanField(default =False)

    natureofContactBriefCheckIn =models.BooleanField(default =False)

    natureofContactFamilyVisitingUnableTosee = models.BooleanField(default =False)

    natureofContactOutOfFacilityOnOuting = models.BooleanField(default =False)

    natureofContactOnvacation = models.BooleanField(default =False)

    natureofContactBreifUpdateOnPatientForFacility = models.BooleanField(default =False)

    natureofContactCalledClientLeftVoicemail = models.BooleanField(default =False)

    natureofContactRescheduleSeesion = models.BooleanField(default =False)

    natureContactUnableToReschedule = models.BooleanField(default =False)

    natureCotactClientGuardianCalledTheOffice =models.BooleanField(default =False)

    natureofContactOther = models.BooleanField(default =False)

    otherAdditionalInformation = models.TextField(default='')

    therapistSignDate = models.DateField(default=date.today)

    therapistSign= models.BooleanField(default =False)


class InitialVisits(models.Model):
    
    LETTER_HEAD_CHOICES =(
            ('1','CHILD NET'),
            ('2','DYNAMIC HEADER'),
        )
    
    # TODO COMPELTE THE LIST
    POSCHOICES = (

        ('1', '02 - TELEHEALTH'),
        ('2', '04 - HOMELESS SHELTER'),
        ('3', '10 - HOME'),
        ('4', '11 - OFFICE'),
        ('5', '13 - ASSISTED LIVING FACILITY'),
        ('6', '21 - INPATIENT HOSPITAL'),
        ('7', '22 - OUTPATIENT HOSPITAL'),
        ('8', '23 - EMERGENCY ROOM HOSPITAL'),
        ('9', '24 - AMBULATORY SURGICAL CENTER'),
        ('10', '25 - BIRTHING CENTER'),
        ('11', '26 - MILITARY TREATMENT FACILITY'),
        ('12', '31 - SKILLED NURSING FACILITY'),
    )

    #TODO diagnostics list
    # ICD codes
     
    ICDCODES =(
        ('1','F31.73- Bipolar disorder, in partial remission, most recent episode manic'),
        ('2', 'F05	Delirium due to another medical condition'),
        ('3', 'F05	Delirium due to multiple etiologies'),
        ('4', 'F06.0	Psychotic disorder due to another medical condition, With hallucinations'),
        ('5', 'F06.1	Catatonia associated with another mental disorder (catatonia specifier)'),
        ('6', 'F06.1	Catatonic disorder due to another medical condition'),
        ('7','F07'),)

    #CPT Code

    CPTCODES = (
        ('1', '99201 - Office_OP New Pat Initial minimum Cmplexity 10 mins'),
        ('2', '99202 - Office_OP New Pat Initial Low Compelexity 20 mins'),
        ('3', '99203 - Office_OP New Pat Initial Moderate Compelexity 30 mins'),
        ('4', '99204 - Office_OP New Pat Initial Comprehensive Compelexity 45 mins'),
        ('5', '99205 - Office_OP New Pat Initial High Compelexity 60 mins'),
        ('6', '99211 - Office_Op Est Pat Follow-Up Minimum Complex 5 mins'),
        ('7', '99212 - Office_Op Est Pat Follow-Up Low Complex 5 mins'),
        ('8', '99213 - Office _OP Est Pat Follow-Up Moderate COmplex 15 mins'),
        ('9', '99214 - Office_OP Est Follow Up Comprehensive Complex 25 mins'),
        ('10','99215 - Office_OP Est Pat Follow-Up High Complex 40 mins'),
        ('11', '99304 - Nursing New Pat Initial Low Complexity 25 mins'),
        ('12', '99305 - Nursing New Pat Initial Moderate Complexity 35 mins'),
        ('13', '99306 - Nursing New Pat Initial High Complexity 45 mins'),
        ('14', '99307 - Nursing Est pat Follow-Up Minimum Complex 10 mins'),
        ('15', '99308 - Nursing Est Pat Fllow-Up Low Complex 15 mins'),
        ('16', '99309 - Nursing Est Pat Follow-Up Moderate Complex 25 mins'),
        ('17', '99310 - Nursing Est Pat Follow-Up High Complex 35 mins'),
        ('18', '99318 - Nursing Est Pat Annual Assessment 60 mins'),
        ('19', '99341 - ALF New Pat New Patient Minimum Complex 15 mins'),
        ('20', '99342 - ALF New Pat New Patient Low Complex 30 mins'), 
        ('21', '99344 - ALF New Pat New Patint Moderate Complex 60 mins'),
        ('22', '99345 - ALF New Pat New Patent Comprehensive Comp. 75 mins'),
        ('23', '99417 - ALF New Pat add on for additional time past High 15 mins'),
        ('24', '99347 - ALF Est Pat Est Pt Min complex 20 mins'),
        ('25', '99348 - ALF Est Pat Est Pt Low COmplex 30 mins'),
        ('26', '99349 - ALF Est Pat Est Pt Moderate Complex 40 mins'),
        ('27', '99350 - ALf Est Pat Est Pt High Complex 60 mins'),
    )

    MODIFIERS = (
        ('1', 'GW - HOSPICE'),
        ('2', '95 - TELEHEALTH'),
    )

    BMIChoices = (
        ('1', 'G8417 - BMI is documented above normal paramters and a follow up plan is documented'),
        ('2', 'G8418 - BMI is documented blow normal paramters and a follow up plan is documented'),
        ('3', 'G8420 - BMI is documented within normal parameters and no follow up plan is required'),
    )

    DOCUMENTATIONOFMEDICALREDORDCHOICES = (
        ('1', 'G8427 - Eligible clinician attests to documenting in the medical record they obtained, updated, reviewed the patients current medications'),
    )

    SCREENINGFORDEPRESSIONCHOICES =(
        ('1', 'G8431 - Screening for depression is documented as positive AND a follow-up plan is documented'),
        ('2', 'G8450 - Screening for depression is documeneted as negative and follow-up plan is not required'),
    )

    ELDERMATREATMENTCHOICES =(
        ('1', 'G8733 - Elder maltreatment screen documented as positive AND a follow up plan is documented'),
        ('2', 'G8734 - Elder maltreatment screen documneted as negative and a follow up treatment is not required'),
    )

    TOBACCOSCRRENINGCHOICES = (
        ('1', 'G9902 - Patient screened for tobacco use AND received tobacco cessation Intervention (counseling, pharmacotherapy or both) if identified tobocco user'),
        ('2', 'Current tobacco non user'),
    )

    HIGHBLOODPRESSURESCREENINGCHOICES = (
        ('1', 'G8783 -  Normal blood pressure reading documented, follow-up not required'),
        ('2', 'G8950 - Pre-Hypertensive or Hypertensive blood pressure is documented AND the indicated follow-up is documented'),
    )

    UNHEALTHYALCOHOLCHOICES = (
        ('1', 'G2196 - Patient identified as an unhelthy alocohol user when screened for unhealthy alcohol use using a systematic screening method'),
        ('2', 'G2197 - Patient screend for unhealthy alcohol use using a systematic screening method AND not identified as an unhealthy alocohol user ')
    )
    mentalRetardation =(
        ('1','Problems with primary support group - Becoming a parent'),
        ('2', 'Problems with primary support group - birth with sibiling'),
        ('3', 'Problems with primary support group - Death of a family member'),
        ('4', 'Problems with primary support group - Discord'),
        ('5', 'Problems with primary support group - Discord with siblings'),
        ('6', 'Problems with primary support group - Disruption of family by separation, divorce or estrangement'),
        ('7', 'Problems with primary support group - Engagement'),
        ('8', 'Problems with primary support group - Friction with child'),
        ('9', 'Problems with primary support group - Health problems in family'),
        ('10','Problems with primary support group - Illness of child'),
        ('11', 'Problems with primary support group - Inadequate dicipline'),
        ('12', 'Problems with primary suppoet group - Long term mental illness'),
        ('13', 'Problems with primary support group - Marriage'),
        ('14', 'Problems with primary support group - Neglect of child'),
        ('15', 'Problems with primary support group - Parental Overprotection'),
        ('16', 'Problems with primary support group - Personal Physical illness or injury'),
        ('17', 'Problems with primary support group - Sexual or Physical abuse'),
        ('18', 'Problems with social related environment - Adjustment to life cycle transition'),
        ('19', 'Problems related to social environment - Death or losst of friend'),
        ('20', 'Problems related to social environment - Difficulties with interpersonal relationship'),
        ('21', 'Problems related to social environment - Difficulty with acculturation'),
        ('22', 'Problems related to social environment - Discrimination'),
        ('23', 'Problems related to social environment - Illness of best friend'),
        ('24', 'Problems related to social environment - Inadequate social support'),
        ('25', 'Problems related to social environment - Living alone'),
        ('26', 'Educational Problems- Academic problems'),
        ('27', 'Educational Problems - Discord with teachers or classmates'),
        ('28', 'Educational Problems - Illiteracy'),
        ('29', 'Educational Problems - School problems'),
        ('30', 'Occupational Problems - Difficult work condition'),
        ('31', 'Occupational Problems - Discord with boss or coworkers'),
        ('32', 'Occupational Problems - Homemaking'),
        ('33', 'Occupational Problems - Job change'),
        ('34', 'Occupational Problems - Job dissatisfaction'),
        ('35', 'Occupational Problems - Stressful work schedule'),
        ('36', 'Occupational Problems - Threat of job loss'),
        ('37', 'Occupational Problems - Unemployment'),
        ('38', 'Housing problems - Change in residence'),
        ('39', 'Housing problems - Discord with neighbors or landlords'),
        ('40', 'Housing problems - Homelessness'),
        ('41', 'Housing problems - immigration'),
        ('42', 'Housing problems - Inadequate housing'),
        ('43', 'Housing problems - Threat to personal safety'),
        ('44', 'Housing problems - Unsafe neighborhood'))
    
    letterhead = models.CharField(max_length=1000, choices= LETTER_HEAD_CHOICES)

    time_in = models.TimeField()

    time_out = models.TimeField()

    dateOfAppointment = models.DateField(default=date.today)

    pos = models.CharField(max_length=1000, choices= POSCHOICES)

    clinicalDisorder = models.CharField(max_length=10000, choices = ICDCODES)

    otherICD10Diagnosis = models.CharField(max_length=1000)

    cptcode = models.CharField(max_length=1000, choices= CPTCODES)

    cptcodeOther1 =models.CharField(max_length=1000)

    unit1 = models.CharField(max_length= 100, default= '')

    modifiers1 =models.CharField(max_length=100, choices=MODIFIERS)

    modifiers2 = models.CharField(max_length=100, choices=MODIFIERS)

    modifiersOther1 = models.CharField(max_length=1000, default ='')

    modifiersOther2 = models.CharField(max_length=1000, default ='')

    bmiScreening = models.CharField(max_length=1000, choices=BMIChoices)

    detailsAndExpInformation =  models.TextField(max_length=10000)

    documentationOfCurrentMedicalRecord = models.CharField(max_length=1000, choices=DOCUMENTATIONOFMEDICALREDORDCHOICES)

    detailsAndExpInformation2 =  models.TextField(max_length=10000)

    screeningForDepresionAndFollowUp = models.CharField(max_length=1000, choices=SCREENINGFORDEPRESSIONCHOICES)

    detailsAndExpInformation3 =  models.TextField(max_length=10000)

    elderMaltreatementScreenFollowup =  models.CharField(max_length=1000, choices=ELDERMATREATMENTCHOICES)

    detailsAndExpInformation4 = models.TextField(max_length=10000)

    tobaccoUseScreeningAndCessation = models.CharField(max_length=1000, choices=TOBACCOSCRRENINGCHOICES)

    detailsAndExpInformation5 = models.TextField(max_length=1000)

    highBloddPressureScreening = models.CharField(max_length=1000, choices=HIGHBLOODPRESSURESCREENINGCHOICES)

    detailsAndExpInformation6 = models.TextField(max_length=1000)

    unhealthyAlcoholUseScrrening = models.CharField(max_length=1000, choices=UNHEALTHYALCOHOLCHOICES)

    detailsAndExpInformation7 = models.TextField(max_length=1000)

    commentsToBillers = models.TextField(max_length=10000)

    #page 2

    letterhead2 = models.CharField(max_length=1000, choices= LETTER_HEAD_CHOICES)

    time_in2 = models.TimeField()

    time_out2 = models.TimeField()

    dateOfAppointment2 = models.DateField(default=date.today)

    pos2 = models.CharField(max_length=1000, choices= POSCHOICES)

    clinicalDisorder2 = models.CharField(max_length=10000, choices = ICDCODES)

    otherICD10Diagnosis2 = models.CharField(max_length=1000)
    
    cptcodepage2 = models.CharField(max_length=1000, choices= CPTCODES)

    cptcodeOther1page2 =models.CharField(max_length=1000)

    unit1page2 = models.CharField(max_length= 100, default= '')

    modifiers1page2 =models.CharField(max_length=100, choices=MODIFIERS)

    modifiers2page2 = models.CharField(max_length=100, choices=MODIFIERS)

    modifiersOther1page2 = models.CharField(max_length=1000, default ='')

    modifiersOther2page2 = models.CharField(max_length=1000, default ='')

    bmiScreeningpage2 = models.CharField(max_length=1000, choices=BMIChoices)

    detailsAndExpInformationpage2 =  models.TextField(max_length=10000)

    documentationOfCurrentMedicalRecordpage2 = models.CharField(max_length=1000, choices=DOCUMENTATIONOFMEDICALREDORDCHOICES)

    detailsAndExpInformation2page2 =  models.TextField(max_length=10000)

    screeningForDepresionAndFollowUppage2 = models.CharField(max_length=1000, choices=SCREENINGFORDEPRESSIONCHOICES)

    detailsAndExpInformation3page2 =  models.TextField(max_length=10000)

    elderMaltreatementScreenFollowuppage2 =  models.CharField(max_length=1000, choices=ELDERMATREATMENTCHOICES)

    detailsAndExpInformation4page2 = models.TextField(max_length=10000)

    tobaccoUseScreeningAndCessationpage2 = models.CharField(max_length=1000, choices=TOBACCOSCRRENINGCHOICES)

    detailsAndExpInformation5page2 = models.TextField(max_length=1000)

    highBloddPressureScreeningpage2 = models.CharField(max_length=1000, choices=HIGHBLOODPRESSURESCREENINGCHOICES)

    detailsAndExpInformation6page2 = models.TextField(max_length=1000)

    unhealthyAlcoholUseScrreningpage2 = models.CharField(max_length=1000, choices=UNHEALTHYALCOHOLCHOICES)

    detailsAndExpInformation7page2 = models.TextField(max_length=1000, default = '')

    commentsToBillerspage2 = models.TextField(max_length=10000, default= '')

    referralSource = models.TextField(max_length=10000, default='')

    reasonForEvaluation = models.TextField(max_length=10000, default='')

    historyOfPresentIllness = models.TextField(max_length=10000, default='')

    patientPrimaryConcern = models.TextField(max_length=10000,default='')

        #Mental Status Examination
    WELLGROOMEDLEVELSChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    UNKEMPTLEVELSCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    DISHEVELEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    eyeCotactAverageLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    eyecontactAvoidantLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    eyecontactIntenseLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    buildAverageLevelChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    buildThinLevelChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    buildOverweightLevelsChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    ACTIVITYAVERAGECHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    ACTIVITYAGITATEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    SLOWEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    #Appearance
    appearanceWellgrommed = models.BooleanField(default=False)
    
    appearanceWellgroomedLevels= models.CharField(max_length=100, choices=WELLGROOMEDLEVELSChoices)
    
    appearanceUnkempt = models.BooleanField(default=False)

    appearanceUnkemptLevels = models.CharField(max_length=100, choices=UNKEMPTLEVELSCHOICES)

    appearanceDisheveled = models.BooleanField(default=False)

    appearanceDisheveledLevels= models.CharField(max_length=100, choices=DISHEVELEDCHOICES)

    #Eye Contact
    eyeCotactAverage = models.BooleanField(default=False)
    
    eyeCotactAverageLevels= models.CharField(max_length=100, choices=eyeCotactAverageLevelsChoices)
    
    eyecontactAvoidant = models.BooleanField(default=False)

    eyecontactAvoidantLevels = models.CharField(max_length=100, choices=eyecontactAvoidantLevelsChoices)

    eyecontactIntense = models.BooleanField(default=False)

    eyecontactIntenseLevels= models.CharField(max_length=100, choices=eyecontactIntenseLevelsChoices)

    
    
    #build
    buildAverage = models.BooleanField(default=False)
    
    buildAverageLevels= models.CharField(max_length=100, choices=buildAverageLevelChoice)
    
    buildThin = models.BooleanField(default=False)

    eyecontacbuildThinLevels = models.CharField(max_length=100, choices=buildThinLevelChoice)

    buildOverweight = models.BooleanField(default=False)

    buildOverweightLevels= models.CharField(max_length=100, choices=buildOverweightLevelsChoice)

    
    #Activity
    activityAverage = models.BooleanField(default=False)
    
    activityAverageLevels= models.CharField(max_length=100, choices=ACTIVITYAVERAGECHOICES)
    
    activityAgitated = models.BooleanField(default=False)

    activityAgitatedLevels = models.CharField(max_length=100, choices=ACTIVITYAGITATEDCHOICES)

    activitySlowed = models.BooleanField(default=False)

    activitySlowedLevels= models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Demeanor

    demeanorAverage = models.BooleanField(default=False)

    demeanorAverageLevels =models.CharField(max_length=100, choices=SLOWEDCHOICES)

    demeanorHostile = models.BooleanField(default=False)

    demeanorHostileLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorMistrustful = models.BooleanField(default=False)

    demeanorMistrustfulLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorWithdrawn = models.BooleanField(default=False)

    demeanorWithdrawnLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorPreoccupied = models.BooleanField(default=False)

    demeanorPreoccupiedLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorDemanding = models.BooleanField(default=False)

    demeanorDemandingLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)


    #Speech

    speechClear = models.BooleanField(default=False)

    speechClearLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechSlurred = models.BooleanField(default=False)

    speechSlurredLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechRapid = models.BooleanField(default=False)

    speechRapidLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechPressured = models.BooleanField(default=False)

    speechPressuredLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Delusions

    delusionsNoneReported = models.BooleanField(default= False)

    delusionsgrandiose = models.BooleanField(default=False)

    delusionsgrandioseLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionspersecutory = models.BooleanField(default= False)

    delusionspersecutoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionssomatic =models.BooleanField(default=False)

    delusionssomaticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsbizarre =models.BooleanField(default=False)

    delusionsbizarreLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsnihilistic = models.BooleanField(default=False)

    delusionsnihilisticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsreligious = models.BooleanField(default=False)

    delusionsreligiouslevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Self Abuse

    selfAbuseNonreported = models.BooleanField(default=False)

    selfAbuseSelfMutilation = models.BooleanField(default=False)

    selfAbuseSelfMutilationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbuseSucidal = models.BooleanField(default=False)

    selfAbuseSucidalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbuseIntent = models.BooleanField(default=False)

    selfAbuseIntentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbusePlan = models.BooleanField(default=False)

    selfAbusePlanLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #other

    otherNoneReported = models.BooleanField(default= False)

    otherAutistic = models.BooleanField(default =False)

    otherAutisticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherObsessional =models.BooleanField(default=False)

    otherObsessionalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPhobic = models.BooleanField(default=False)

    otherPhobicLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherGuilty = models.BooleanField(default=False)

    otherGuiltyLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherIdeasOfreference = models.BooleanField(default= False)

    otherIdeasOfreferenceLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES) 

    otherPreoccupied = models.BooleanField(default=False)

    otherPreoccupiedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherGuraded = models.BooleanField(default=False)

    otherGuradedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherOption = models.BooleanField(default=False)

    otherOptionText = models.CharField(max_length=1000)

    #Aggressive

    aggressiveNoneReported = models.BooleanField(default=False)

    aggressiveHomicidal = models.BooleanField(default=False)

    aggressiveHomicidalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    aggresiveIntent = models.BooleanField(default=False)

    aggresiveIntentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    aggressivePlan = models.BooleanField(default=False)

    aggressivePlanLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    
    
    #Perception/Hallucinations

    hallucinationsNoneReported = models.BooleanField(default= False)

    hallucinationsAuditory = models.BooleanField(default=False)

    hallucinationsAuditoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsVisual = models.BooleanField(default= False)

    hallucinationsVisualLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsOlfactory = models.BooleanField(default=False)

    hallucinationsOlfactoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsGustatory = models.BooleanField(default = False)

    hallucinationsGustatoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsTactile = models.BooleanField(default= False)

    hallucinationsTactileLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Other/Perception

    otherPerceptionNonreported = models.BooleanField(default= False)

    otherPerceptionIllusions = models.BooleanField(default =False)

    otherPerceptionIllusionsLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPerceptionDepersonalization = models.BooleanField(default=False)

    otherPerceptionDepersonalizationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPerceptionDerealization = models.BooleanField(default=False)

    otherPerceptionDerealizationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Thought Process

    thoughtProcessLogical = models.BooleanField(default= False)
    
    thoughtProcessLogicalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessCircumstantial = models.BooleanField(default = False)

    thoughtProcessCircumstantialLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessTangential = models.BooleanField(default= False)

    thoughtProcessTangentialLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessLoose = models.BooleanField(default=False)

    thoughtProcessLooseLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessRacing = models.BooleanField(default= False)

    thoughtProcessRacingLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessIncoherent = models.BooleanField(default= False)

    thoughtProcessIncoherentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessConcrete = models.BooleanField(default= False)

    thoughtProcessConcreteLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessBlocked = models.BooleanField(default= False)

    thoughtProcessBlockedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessFlightOfIdeas = models.BooleanField(default= False)

    thoughtProcessFlightOfIdeasLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #mood

    moodEuthymic = models.BooleanField(default= False)

    moodEuthymicLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodDepressed = models.BooleanField(default= False)

    moodDepressedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodAnxious = models.BooleanField(default= False)

    moodAnxiousLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodAngry = models.BooleanField(default= False)

    moodAngryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodEuphoric = models.BooleanField(default= False)
    
    moodEuphoricLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodIrritable = models.BooleanField(default= False)

    moodIrritableLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Affect

    affectFull = models.BooleanField(default= False)

    affectFullLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectConstricted = models.BooleanField(default= False)

    affectConstrictedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectFlat = models.BooleanField(default= False)

    affectFlatLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectInappropriate = models.BooleanField(default= False)

    affectInappropriateLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectLabile = models.BooleanField(default= False)

    affectLabileLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Behavior

    behaviorCooperative = models.BooleanField(default= False)

    behaviorCooperativelevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorResistant = models.BooleanField(default= False)

    behaviorResistantLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAgitated = models.BooleanField(default= False)

    behaviorAgitatedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorImpulsive = models.BooleanField(default= False)

    behaviorImpulsiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorOverSedated = models.BooleanField(default= False)

    behaviorOverSedatedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    
    #
    behaviorAssaultive = models.BooleanField(default= False)

    behaviorAssaultiveLevels =models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAggresive = models.BooleanField(default= False)

    behaviorAggresiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorHyperactive = models.BooleanField(default= False)

    behaviorHyperactiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorRestless = models.BooleanField(default= False)

    behaviorRestlessLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorLossOfInterest = models.BooleanField(default= False)

    behaviorLossOfInterestLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    #
    behaviorAnhedonia = models.BooleanField(default= False)
    
    behaviorAnhedoniaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAkasthisia = models.BooleanField(default= False)

    behaviorAkasthisiaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorWithdrawn = models.BooleanField(default= False)

    behaviorWithdrawnLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorDystonia = models.BooleanField(default= False)

    behaviorDystoniaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorTardive = models.BooleanField(default= False)

    behaviorTardiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorDyskinesia = models.BooleanField(default= False)

    behaviorDyskinesiaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Cognition

    impairmentofNonReported = models.BooleanField(default= False)

    impairmentofOrientation = models.BooleanField(default= False)

    impairmentofOrientationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofMemory = models.BooleanField(default= False)

    impairmentofMemoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofAttentionConcentration = models.BooleanField(default= False)

    impairmentofAttentionConcentrationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofAbilityToAbstract = models.BooleanField(default= False)

    impairmentofAbilityToAbstractLevels = models.CharField(max_length=100, choices= SLOWEDCHOICES)

    #Intelligence

    IntelligenceMR = models.BooleanField(default= False)

    IntelligenceMRLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceBorderline = models.BooleanField(default= False)

    IntelligenceBorderlineLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceAverage = models.BooleanField(default= False)

    IntelligenceAverageLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceAboveAverage = models.BooleanField(default= False)

    IntelligenceAboveAverageLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Judgement/Insight

    InsightWithinNormalLimits = models.BooleanField(default=False)

    InsightMildImpairment  = models.BooleanField(default=False)

    InsightModerateImpairment = models.BooleanField(default=False)

    InsightSevereImpairment = models.BooleanField(default=False)

    #Memory

    MemoryWithinNormalLimits = models.BooleanField(default=False)

    MemoryMildImpairment  = models.BooleanField(default=False)

    MemoryModerateImpairment = models.BooleanField(default=False)

    MemorySevereImpairment = models.BooleanField(default=False)

    #Sleeping Patterns

    sleepingPatternsAdequate = models.BooleanField(default=False)

    sleepingPatternsInsufficient = models.BooleanField(default=False)

    sleepingPatternsDisturbed = models.BooleanField(default=False)

    #Eating Patterns:

    eatingPatternsWithinNormalLimits = models.BooleanField(default =False)

    eatingPatternsUndereating = models.BooleanField(default=False)

    eatingPatternsOvereating = models.BooleanField(default=False)

    #Thought content
    
    thoughtContentWithinNormalLimits = models.BooleanField(default=False)

    thoughtContentPreoccupied = models.BooleanField(default=False)

    thoughtContentObsessive = models.BooleanField(default=False)

    thoughtContentGuarded = models.BooleanField(default=False)

    thoughtContentideasOfreference = models.BooleanField(default=False)

    thoughtContentGuilty = models.BooleanField(default=False)

    thoughtContentScared = models.BooleanField(default=False)


    #Suicidality/Homocidlity
    suicidalityNonReported = models.BooleanField(default=False)

    suicidalitySelfMutilation = models.BooleanField(default=False)


    #Suicidality
    suicidalityNonreported = models.BooleanField(default=False)

    suicidalityIntent = models.BooleanField(default=False)

    suicidalityPassiveIdeation = models.BooleanField(default=False)

    suicidalityPlan = models.BooleanField(default=False)

    suicidalityMeans = models.BooleanField(default=False)

    #orientation

    orientationPersonOnly = models.BooleanField(default=False)

    orientationPersonOnly = models.BooleanField(default=False)

    orientationSituationTeam =models.BooleanField(default=False)

    orientationTimeOnly = models.BooleanField(default=False)

    
    mentalStatusExaminationField = models.TextField(max_length=10000, default='')


    #miniMentalStatusExamination

    minimentalexamnationScore = models.CharField(max_length=10000,default='')

    #orientation
    orientationPerson = models.BooleanField(default=False)
    
    orientationPlace = models.BooleanField(default=False)

    orientationTime = models.BooleanField(default=False)

    orientationDate = models.BooleanField(default=False)

    #Attention

    attentionNormal = models.BooleanField(default=False)

    attentionMildlyImpaired = models.BooleanField(default=False)

    attentionModeratelyImpaired = models.BooleanField(default=False)

    attentionSeverelyImpaired = models.BooleanField(default=False)

    #memory

    memoryNormal = models.BooleanField(default=False)

    memoryMildlyImpaired = models.BooleanField(default=False)

    memoryModeratelyImpaired = models.BooleanField(default=False)

    memorySeverelyImpaired = models.BooleanField(default=False)

    #language

    languageNormal = models.BooleanField(default=False)

    languageMildlyImpaired = models.BooleanField(default=False)

    languageModeratelyImpaired = models.BooleanField(default=False)

    languageSeverelyImpaired = models.BooleanField(default=False)

    #Visual

    visualNormal = models.BooleanField(default=False)

    visualMildlyImpaired = models.BooleanField(default=False)

    visualModeratelyImapired = models.BooleanField(default=False)

    visualSeverelyImpaired = models.BooleanField(default=False)


    #scores

    ScoreNormal = models.BooleanField(default=False)

    ScoreMildImpairment = models.BooleanField(default=False)
    
    scoreMopderate = models.BooleanField(default=False)

    scoreSevere = models.BooleanField(default=False)

    #history

    socialFamily = models.TextField(max_length=10000, default='')

    socialMedicalHistory =models.TextField(max_length=10000, default='')

    significantAlcoholHistory = models.BooleanField(default=False)

    significantalcohol = models.BooleanField(default=False)

    significantDrugs = models.BooleanField(default=False)

    significantTobbaco = models.BooleanField(default=False)

    significantTobbaccoField = models.TextField(max_length=10000, default='')

    levelOfDailyFunctioning = models.TextField(max_length=10000, default='')

    medicalNecessity = models.TextField(max_length=10000, default='')

    notappropriateForPsychologicalService = models.BooleanField(default=False)

    individualTherapy = models.BooleanField(default=False)

    groupTherapy = models.BooleanField(default=False)

    familyTherapy =models.BooleanField(default=False)

    otherRecommendation = models.CharField(max_length=10000,default='')

    forEvaluationAnxiety = models.BooleanField(default=False)

    forEvaluationBehavior = models.BooleanField(default =False)

    forEvaluationCognativeSkills = models.BooleanField(default=False)

    forEvaluationDepression = models.BooleanField(default=False)

    forEvaluationEmotionalStatus = models.BooleanField(default=False)

    forEvaluationOther = models.CharField(max_length=10000, default='')

    externalPsychiatricReferral = models.BooleanField(default=False)

    externalPsychiatricReferralCharField = models.CharField(max_length=1000, default='')

    familyconferenceCheckbox = models.BooleanField(default =False)

    emotionalBehaviorFUnctionTextfield = models.TextField(max_length=10000, default=False)

    strengths = models.TextField(max_length=10000, default='')

    liabilities = models.TextField(max_length=10000, default='')

    generalMedicalCondition = models.TextField(max_length=10000, default='')

    psychologicalEnvironmentChoiceField = models.CharField(max_length=1000, choices=mentalRetardation)

    otherDiagnosis = models.CharField(max_length=1000, default= '')

    #treatment frequency
    FREQUENCY = (
        ('1', 'Day'),
        ('2', 'Week'),
        ('3', 'Month'),
        ('4', 'Quarter'),
        ('5', 'Year'),
    )

    treatmentIndividual = models.BooleanField(default=False)

    individualcharfield = models.CharField(max_length=1000, default='')

    treatmentFrequncyPer =models.CharField(max_length=100,default='')

    grouptreatmentCheckbox = models.BooleanField(default=False)

    groupCharfield = models.CharField(max_length=100, default='')

    groupChoices = models.CharField(max_length=100, choices=FREQUENCY)

    estimatedNumberOfSession = models.CharField(max_length=100, default='')
 

    #treatmenmt plan

    treatmentFrequencyStartDate1 = models.DateField()

    treatmentPlanReviewDate1 = models.DateField()

    goalsAndObjectives1 = models.TextField(max_length=10000, default='')

    treatmentFrequencyStartDate2 = models.DateField()

    treatmentFrequencyReviewDate2 = models.DateField()

    goalsAndObjectives2 = models.TextField(max_length=10000, default='')

    treatmentFrequencyStartDate3 = models.DateField()

    treatmentFrequencyReviewDate3 = models.DateField()

    goalsAndObjectives3 = models.TextField(max_length=10000, default='')

    treatmentFrequencyStartDate4 = models.DateField()

    treatmentFrequencyReviewDate4 = models.DateField()

    goalsAndObjectives4 = models.TextField(max_length=10000, default='')

    generalNoteTestResult =models.TextField(max_length=10000, default='')

    therapistsigndate= models.DateField(default=date.today)


class ProgressNote(models.Model):
    
    LETTER_HEAD_CHOICES =(
            ('1','CHILD NET'),
            ('2','DYNAMIC HEADER'),
        )
    
    # TODO COMPELTE THE LIST
    POSCHOICES = (

        ('1', '02 - TELEHEALTH'),
        ('2', '04 - HOMELESS SHELTER'),
        ('3', '10 - HOME'),
        ('4', '11 - OFFICE'),
        ('5', '13 - ASSISTED LIVING FACILITY'),
        ('6', '21 - INPATIENT HOSPITAL'),
        ('7', '22 - OUTPATIENT HOSPITAL'),
        ('8', '23 - EMERGENCY ROOM HOSPITAL'),
        ('9', '24 - AMBULATORY SURGICAL CENTER'),
        ('10', '25 - BIRTHING CENTER'),
        ('11', '26 - MILITARY TREATMENT FACILITY'),
        ('12', '31 - SKILLED NURSING FACILITY'),
    )

    #TODO diagnostics list
    # ICD codes
     
    ICDCODES =(
        ('1','F31.73- Bipolar disorder, in partial remission, most recent episode manic'),
        ('2', 'F05	Delirium due to another medical condition'),
        ('3', 'F05	Delirium due to multiple etiologies'),
        ('4', 'F06.0	Psychotic disorder due to another medical condition, With hallucinations'),
        ('5', 'F06.1	Catatonia associated with another mental disorder (catatonia specifier)'),
        ('6', 'F06.1	Catatonic disorder due to another medical condition'),
        ('7','F07'),)

    #CPT Code

    CPTCODES = (
        ('1', '99201 - Office_OP New Pat Initial minimum Cmplexity 10 mins'),
        ('2', '99202 - Office_OP New Pat Initial Low Compelexity 20 mins'),
        ('3', '99203 - Office_OP New Pat Initial Moderate Compelexity 30 mins'),
        ('4', '99204 - Office_OP New Pat Initial Comprehensive Compelexity 45 mins'),
        ('5', '99205 - Office_OP New Pat Initial High Compelexity 60 mins'),
        ('6', '99211 - Office_Op Est Pat Follow-Up Minimum Complex 5 mins'),
        ('7', '99212 - Office_Op Est Pat Follow-Up Low Complex 5 mins'),
        ('8', '99213 - Office _OP Est Pat Follow-Up Moderate COmplex 15 mins'),
        ('9', '99214 - Office_OP Est Follow Up Comprehensive Complex 25 mins'),
        ('10','99215 - Office_OP Est Pat Follow-Up High Complex 40 mins'),
        ('11', '99304 - Nursing New Pat Initial Low Complexity 25 mins'),
        ('12', '99305 - Nursing New Pat Initial Moderate Complexity 35 mins'),
        ('13', '99306 - Nursing New Pat Initial High Complexity 45 mins'),
        ('14', '99307 - Nursing Est pat Follow-Up Minimum Complex 10 mins'),
        ('15', '99308 - Nursing Est Pat Fllow-Up Low Complex 15 mins'),
        ('16', '99309 - Nursing Est Pat Follow-Up Moderate Complex 25 mins'),
        ('17', '99310 - Nursing Est Pat Follow-Up High Complex 35 mins'),
        ('18', '99318 - Nursing Est Pat Annual Assessment 60 mins'),
        ('19', '99341 - ALF New Pat New Patient Minimum Complex 15 mins'),
        ('20', '99342 - ALF New Pat New Patient Low Complex 30 mins'), 
        ('21', '99344 - ALF New Pat New Patint Moderate Complex 60 mins'),
        ('22', '99345 - ALF New Pat New Patent Comprehensive Comp. 75 mins'),
        ('23', '99417 - ALF New Pat add on for additional time past High 15 mins'),
        ('24', '99347 - ALF Est Pat Est Pt Min complex 20 mins'),
        ('25', '99348 - ALF Est Pat Est Pt Low COmplex 30 mins'),
        ('26', '99349 - ALF Est Pat Est Pt Moderate Complex 40 mins'),
        ('27', '99350 - ALf Est Pat Est Pt High Complex 60 mins'),
    )

    MODIFIERS = (
        ('1', 'GW - HOSPICE'),
        ('2', '95 - TELEHEALTH'),
    )

    BMIChoices = (
        ('1', 'G8417 - BMI is documented above normal paramters and a follow up plan is documented'),
        ('2', 'G8418 - BMI is documented blow normal paramters and a follow up plan is documented'),
        ('3', 'G8420 - BMI is documented within normal parameters and no follow up plan is required'),
    )

    DOCUMENTATIONOFMEDICALREDORDCHOICES = (
        ('1', 'G8427 - Eligible clinician attests to documenting in the medical record they obtained, updated, reviewed the patients current medications'),
    )

    SCREENINGFORDEPRESSIONCHOICES =(
        ('1', 'G8431 - Screening for depression is documented as positive AND a follow-up plan is documented'),
        ('2', 'G8450 - Screening for depression is documeneted as negative and follow-up plan is not required'),
    )

    ELDERMATREATMENTCHOICES =(
        ('1', 'G8733 - Elder maltreatment screen documented as positive AND a follow up plan is documented'),
        ('2', 'G8734 - Elder maltreatment screen documneted as negative and a follow up treatment is not required'),
    )

    TOBACCOSCRRENINGCHOICES = (
        ('1', 'G9902 - Patient screened for tobacco use AND received tobacco cessation Intervention (counseling, pharmacotherapy or both) if identified tobocco user'),
        ('2', 'Current tobacco non user'),
    )

    HIGHBLOODPRESSURESCREENINGCHOICES = (
        ('1', 'G8783 -  Normal blood pressure reading documented, follow-up not required'),
        ('2', 'G8950 - Pre-Hypertensive or Hypertensive blood pressure is documented AND the indicated follow-up is documented'),
    )

    UNHEALTHYALCOHOLCHOICES = (
        ('1', 'G2196 - Patient identified as an unhelthy alocohol user when screened for unhealthy alcohol use using a systematic screening method'),
        ('2', 'G2197 - Patient screend for unhealthy alcohol use using a systematic screening method AND not identified as an unhealthy alocohol user ')
    )
    letterhead = models.CharField(max_length=1000, choices= LETTER_HEAD_CHOICES)

    time_in = models.TimeField()

    time_out = models.TimeField()

    dateOfAppointment = models.DateField(default=date.today)

    pos = models.CharField(max_length=1000, choices= POSCHOICES)

    clinicalDisorder = models.CharField(max_length=10000, choices = ICDCODES)

    otherICD10Diagnosis = models.CharField(max_length=1000)

    cptcode = models.CharField(max_length=1000, choices= CPTCODES)

    cptcodeOther1 =models.CharField(max_length=1000)

    unit1 = models.CharField(max_length= 100, default= '')

    modifiers1 =models.CharField(max_length=100, choices=MODIFIERS)

    modifiers2 = models.CharField(max_length=100, choices=MODIFIERS)

    modifiersOther1 = models.CharField(max_length=1000, default ='')

    modifiersOther2 = models.CharField(max_length=1000, default ='')

    bmiScreening = models.CharField(max_length=1000, choices=BMIChoices)

    detailsAndExpInformation =  models.TextField(max_length=10000)

    documentationOfCurrentMedicalRecord = models.CharField(max_length=1000, choices=DOCUMENTATIONOFMEDICALREDORDCHOICES)

    detailsAndExpInformation2 =  models.TextField(max_length=10000)

    screeningForDepresionAndFollowUp = models.CharField(max_length=1000, choices=SCREENINGFORDEPRESSIONCHOICES)

    detailsAndExpInformation3 =  models.TextField(max_length=10000)

    elderMaltreatementScreenFollowup =  models.CharField(max_length=1000, choices=ELDERMATREATMENTCHOICES)

    detailsAndExpInformation4 = models.TextField(max_length=10000)

    tobaccoUseScreeningAndCessation = models.CharField(max_length=1000, choices=TOBACCOSCRRENINGCHOICES)

    detailsAndExpInformation5 = models.TextField(max_length=1000)

    highBloddPressureScreening = models.CharField(max_length=1000, choices=HIGHBLOODPRESSURESCREENINGCHOICES)

    detailsAndExpInformation6 = models.TextField(max_length=1000)

    unhealthyAlcoholUseScrrening = models.CharField(max_length=1000, choices=UNHEALTHYALCOHOLCHOICES)

    detailsAndExpInformation7 = models.TextField(max_length=1000)

    commentsToBillers = models.TextField(max_length=10000)

class TreatmentPlan(models.Model):

    LETTER_HEAD_CHOICES =(
            ('1','CHILD NET'),
            ('2','DYNAMIC HEADER'),
        )
    TREATMENTPLANFREQCHOICES =(
        ('1', 'Day'),
        ('2', 'Week'),
        ('3', 'Month'),
        ('4', 'Quarter'),
        ('5', 'Year'),
    )

         
    ICDCODES =(
        ('1','F31.73- Bipolar disorder, in partial remission, most recent episode manic'),
        ('2', 'F05	Delirium due to another medical condition'),
        ('3', 'F05	Delirium due to multiple etiologies'),
        ('4', 'F06.0	Psychotic disorder due to another medical condition, With hallucinations'),
        ('5', 'F06.1	Catatonia associated with another mental disorder (catatonia specifier)'),
        ('6', 'F06.1	Catatonic disorder due to another medical condition'),
        ('7','F07'),)
    

    letterhead = models.CharField(max_length=1000, choices= LETTER_HEAD_CHOICES)

    time_in = models.TimeField()

    time_out = models.TimeField()

    dateOfAppointment = models.DateField(default=date.today)

    individualTreatmentPlan = models.BooleanField(default= False)
    
    treatmentFrequencyIndividual = models.IntegerField()

    treatmentIndividualDays = models.CharField(max_length=1000, choices=TREATMENTPLANFREQCHOICES)

    groupTreatmentPlan = models.BooleanField(default= False)

    groupFrequency = models.IntegerField()

    groupDays = models.CharField(max_length=1000, choices=TREATMENTPLANFREQCHOICES)

    numberOfSessionsToAcheieveObjectives = models.IntegerField()

    treatmentPlanStartDate1 = models.DateField(default=date.today)

    treatmentPlanReviewDate1 = models.DateField(default=date.today)

    treatmentPlanNew = models.BooleanField(default= False)

    treatmentPlanContinue = models.BooleanField(default = False)

    treatmentPlanDefer =models.BooleanField(default =False)

    treatmentPlanAchieve =models.BooleanField(default = False)

    currentGoalObjectives1 = models.TextField(max_length=10000)

    progess1 = models.TextField(max_length=10000)

    updatedGoalobjectives1 = models.TextField(max_length=10000)

    treatmentPlanStartDate2 = models.DateField(default=date.today)

    treatmentPlanReviewDate2 = models.DateField(default=date.today)
    
    treatmentPlanNew2 = models.BooleanField(default= False)

    treatmentPlanContinue2 = models.BooleanField(default = False)

    treatmentPlanDefer2 =models.BooleanField(default =False)

    treatmentPlanAchieve2 =models.BooleanField(default = False)

    currentGoalObjectives2 = models.TextField(max_length=10000)

    progess2 = models.TextField(max_length=10000)

    updatedGoalobjectives2 = models.TextField(max_length=10000)

 
    treatmentPlanStartDate3 = models.DateField(default=date.today)

    treatmentPlanReviewDate3 = models.DateField(default=date.today)
    
    treatmentPlanNew3 = models.BooleanField(default= False)

    treatmentPlanContinue3 = models.BooleanField(default = False)

    treatmentPlanDefer3 =models.BooleanField(default =False)

    treatmentPlanAchieve3 =models.BooleanField(default = False)

    currentGoalObjectives3 = models.TextField(max_length=10000)

    progess3 = models.TextField(max_length=10000)

    updatedGoalobjectives3 = models.TextField(max_length=10000)


    treatmentPlanStartDate4 = models.DateField(default=date.today)

    treatmentPlanReviewDate4 = models.DateField(default=date.today)
    
    treatmentPlanNew4 = models.BooleanField(default= False)

    treatmentPlanContinue4 = models.BooleanField(default = False)

    treatmentPlanDefer4 =models.BooleanField(default =False)

    treatmentPlanAchieve4 =models.BooleanField(default = False)

    currentGoalObjectives4 = models.TextField(max_length=10000)

    progess4 = models.TextField(max_length=10000)

    updatedGoalobjectives4 = models.TextField(max_length=10000)


    clinicalDisorders = models.CharField(max_length=1000, choices=ICDCODES)

    otherDiagnosis = models.CharField(max_length=1000)

    comments = models.TextField(max_length=10000)

    therapistSignDate = models.DateField(default=date.today)

class PsychiatricEvaluationAdult(models.Model):

    LETTER_HEAD_CHOICES =(
            ('1','CHILD NET'),
            ('2','DYNAMIC HEADER'),
        )
    
    POSCHOICES = (

        ('1', '02 - TELEHEALTH'),
        ('2', '04 - HOMELESS SHELTER'),
        ('3', '10 - HOME'),
        ('4', '11 - OFFICE'),
        ('5', '13 - ASSISTED LIVING FACILITY'),
        ('6', '21 - INPATIENT HOSPITAL'),
        ('7', '22 - OUTPATIENT HOSPITAL'),
        ('8', '23 - EMERGENCY ROOM HOSPITAL'),
        ('9', '24 - AMBULATORY SURGICAL CENTER'),
        ('10', '25 - BIRTHING CENTER'),
        ('11', '26 - MILITARY TREATMENT FACILITY'),
        ('12', '31 - SKILLED NURSING FACILITY'),
    )

    SEXCHOICES =(
        ('1', 'Male'),
        ('2', 'Female'),
    )

    RACECHOICES = (
        ('1','Caucasian'),
        ('2', 'Latino'),
        ('3', 'Asian'),
        ('4', 'African American'),
        ('5', 'Other'),
    )

    MARITALSTATUSCHOICES = (
        ('1', 'Married'),
        ('2', 'Single'),
        ('3', 'Widowed'),
        ('4', 'Divorced'),
    )
    letterhead = models.CharField(max_length=1000, choices= LETTER_HEAD_CHOICES)

    clientName = models.CharField(max_length=1000)

    dateOfAppointment = models.DateField(default=date.today)

    time_in = models.TimeField()

    time_out = models.TimeField()

    totalHour = models.CharField(max_length=1000)

    pos = models.CharField(max_length=1000, choices= POSCHOICES)

    sex = models.CharField(max_length=100, choices=SEXCHOICES)

    age = models.IntegerField()

    race = models.CharField(max_length=1000, choices = RACECHOICES)

    maritalStatus = models.CharField(max_length=1000, choices= MARITALSTATUSCHOICES)

    referralSource = models.CharField(max_length=1000)

    referralSourceNA =models.BooleanField(default =False)

    clientPresent = models.BooleanField(default=False)

    othersPresent = models.BooleanField(default = False)

    relationshipToClientName = models.CharField(max_length=1000)

    relationshipToClientRelationship = models.CharField(max_length=1000)

    relationshipToClientName2 = models.CharField(max_length=1000)

    relationshipToClientRelationship2 = models.CharField(max_length=1000)

    relationshipToClientName3 = models.CharField(max_length=1000)

    relationshipToClientRelationship3 = models.CharField(max_length=1000)

    presentingPsychiatricProblemAndHistory = models.TextField(max_length=1000)

    smoker = models.BooleanField(default=False)
    
    nonSmoker = models.BooleanField(default = False)

    broachuresAndCounselingGivenForSmoking = models.BooleanField(default= False)

    schizophrenia = models.BooleanField(default = False)

    bipolarDisorder = models.BooleanField(default=False)

    depression = models.BooleanField(default= False)

    anxietyDisorder = models.BooleanField(default =False)

    addDisorder = models.BooleanField(default =False)

    substanceAbuse = models.BooleanField(default =False)

    otherDisorders = models.BooleanField(default= False)

    naDisorders = models.BooleanField(default =False)

    comment = models.CharField(max_length=10000)

    pastPyschiatricReviewDate = models.DateField()

    pastPsychiatricNoHistory = models.BooleanField(default =False)

    pastPsychiatricAdditionalHistory = models.BooleanField(default=False)

    pastPyschiatriInformationIndicated = models.BooleanField(default= False)

    hospitalizationsNA = models.BooleanField(default = False)

    hospitalizations1 = models.CharField(max_length=1000)

    hospitalizationsdate1 = models.DateField()

    hospitalizations2 = models.CharField(max_length=1000)

    hospitalizationsdate2 = models.DateField()

    hospitalizations3 = models.CharField(max_length=1000)

    hospitalizationsdate3 = models.DateField()

    hospitalizations4 = models.CharField(max_length=1000)

    hospitalizationsdate4 = models.DateField()

    outpatientTreatmentNA = models.BooleanField(default =False)

    outpatientTreatment1 = models.CharField(max_length=1000)

    outpatientTreatmentDate1 = models.DateField()

    outpatientTreatment2 = models.CharField(max_length=1000)

    outpatientTreatmentDate2 =models.DateField()

    outpatientTreatment3 = models.CharField(max_length=1000)

    outpatientTreatmentDate3 = models.DateField()

    outpatientTreatment4 = models.CharField(max_length=1000)

    outpatientTreatmentDate4 = models.DateField()

    currentMedicationDate = models.DateField()

    noAdditionalCurrentmedicationNeeded = models.BooleanField(default=False)

    additionalMedicationNeeded = models.BooleanField(default=False)

    informationIdicated = models.BooleanField(default=False)                           
    
    currentMedication1 = models.CharField(max_length=1000)

    rationale1 = models.CharField(max_length=1000)

    dosage1 = models.CharField(max_length=1000)

    complianceYes1 =models.BooleanField(default=False)

    complianceNo1 = models.BooleanField(default=False)

    compliancePartial1 = models.BooleanField(default=False)

    complianceUnknown1 =models.BooleanField(default= False)

    currentMedication2 = models.CharField(max_length=1000)

    rationale2 = models.CharField(max_length=1000)

    dosage2 = models.CharField(max_length=1000)

    complianceYes2 =models.BooleanField(default=False)

    complianceNo2 = models.BooleanField(default=False)

    compliancePartial2 = models.BooleanField(default=False)

    complianceUnknown2 =models.BooleanField(default= False)

    currentMedication3 = models.CharField(max_length=1000)

    rationale3 = models.CharField(max_length=1000)

    dosage3 = models.CharField(max_length=1000)

    complianceYes3 =models.BooleanField(default=False)

    complianceNo3 = models.BooleanField(default=False)

    compliancePartial3 = models.BooleanField(default=False)

    complianceUnknown3 =models.BooleanField(default= False)

    currentMedication4 = models.CharField(max_length=1000)

    rationale4 = models.CharField(max_length=1000)
    
    dosage4 = models.CharField(max_length=1000)

    complianceYes4 =models.BooleanField(default=False)

    complianceNo4 = models.BooleanField(default=False)

    compliancePartial4 = models.BooleanField(default=False)

    complianceUnknown4 =models.BooleanField(default= False)

    currentMedication5 = models.CharField(max_length=1000)

    rationale5 = models.CharField(max_length=1000)

    dosage5 = models.CharField(max_length=1000)

    complianceYes5 =models.BooleanField(default=False)

    complianceNo5 = models.BooleanField(default=False)

    compliancePartial5 = models.BooleanField(default=False)

    complianceUnknown5 =models.BooleanField(default= False)

    medicationSideeffectsNonReported = models.BooleanField(default=False)

    medicationSideeffects = models.TextField(max_length=1000)

    adverseDrugReactionsAllergiesNA = models.BooleanField(default=False)

    adverseDrugReactionsAllergies = models.TextField(max_length=1000)

    psychiatricSocialHistory = models.DateField()

    noAdditionalPsychiatricSocialHistory = models.BooleanField(default=False)

    additionalPsychiatricSocialHistory = models.BooleanField(default=False)

    informationIdicatedBelow2 = models.BooleanField(default=False)

    additionalPsychiatricHitory = models.TextField(max_length=1000)

    healthHistoryDate = models.DateField()

    noAdditionalhealthHistoryNoted = models.BooleanField(default=1000)

    additionalHistorybelow = models.BooleanField(default=False)

    informationIndicatedBelow3 = models.BooleanField(default = False)

        #Mental Status Examination
    WELLGROOMEDLEVELSChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    UNKEMPTLEVELSCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    DISHEVELEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    eyeCotactAverageLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    eyecontactAvoidantLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    eyecontactIntenseLevelsChoices = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    buildAverageLevelChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    buildThinLevelChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    buildOverweightLevelsChoice = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    ACTIVITYAVERAGECHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    ACTIVITYAGITATEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    SLOWEDCHOICES = (
            ('1','1'),
            ('2', '2'),
            ('3', '3'),
        )
    
    #Appearance
    appearanceWellgrommed = models.BooleanField(default=False)
    
    appearanceWellgroomedLevels= models.CharField(max_length=100, choices=WELLGROOMEDLEVELSChoices)
    
    appearanceUnkempt = models.BooleanField(default=False)

    appearanceUnkemptLevels = models.CharField(max_length=100, choices=UNKEMPTLEVELSCHOICES)

    appearanceDisheveled = models.BooleanField(default=False)

    appearanceDisheveledLevels= models.CharField(max_length=100, choices=DISHEVELEDCHOICES)

    #Eye Contact
    eyeCotactAverage = models.BooleanField(default=False)
    
    eyeCotactAverageLevels= models.CharField(max_length=100, choices=eyeCotactAverageLevelsChoices)
    
    eyecontactAvoidant = models.BooleanField(default=False)

    eyecontactAvoidantLevels = models.CharField(max_length=100, choices=eyecontactAvoidantLevelsChoices)

    eyecontactIntense = models.BooleanField(default=False)

    eyecontactIntenseLevels= models.CharField(max_length=100, choices=eyecontactIntenseLevelsChoices)

    
    
    #build
    buildAverage = models.BooleanField(default=False)
    
    buildAverageLevels= models.CharField(max_length=100, choices=buildAverageLevelChoice)
    
    buildThin = models.BooleanField(default=False)

    eyecontacbuildThinLevels = models.CharField(max_length=100, choices=buildThinLevelChoice)

    buildOverweight = models.BooleanField(default=False)

    buildOverweightLevels= models.CharField(max_length=100, choices=buildOverweightLevelsChoice)

    
    #Activity
    activityAverage = models.BooleanField(default=False)
    
    activityAverageLevels= models.CharField(max_length=100, choices=ACTIVITYAVERAGECHOICES)
    
    activityAgitated = models.BooleanField(default=False)

    activityAgitatedLevels = models.CharField(max_length=100, choices=ACTIVITYAGITATEDCHOICES)

    activitySlowed = models.BooleanField(default=False)

    activitySlowedLevels= models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Demeanor

    demeanorAverage = models.BooleanField(default=False)

    demeanorAverageLevels =models.CharField(max_length=100, choices=SLOWEDCHOICES)

    demeanorHostile = models.BooleanField(default=False)

    demeanorHostileLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorMistrustful = models.BooleanField(default=False)

    demeanorMistrustfulLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorWithdrawn = models.BooleanField(default=False)

    demeanorWithdrawnLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorPreoccupied = models.BooleanField(default=False)

    demeanorPreoccupiedLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)

    demeanorDemanding = models.BooleanField(default=False)

    demeanorDemandingLevels = models.CharField(max_length=100 , choices= SLOWEDCHOICES)


    #Speech

    speechClear = models.BooleanField(default=False)

    speechClearLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechSlurred = models.BooleanField(default=False)

    speechSlurredLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechRapid = models.BooleanField(default=False)

    speechRapidLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    speechPressured = models.BooleanField(default=False)

    speechPressuredLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Delusions

    delusionsNoneReported = models.BooleanField(default= False)

    delusionsgrandiose = models.BooleanField(default=False)

    delusionsgrandioseLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionspersecutory = models.BooleanField(default= False)

    delusionspersecutoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionssomatic =models.BooleanField(default=False)

    delusionssomaticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsbizarre =models.BooleanField(default=False)

    delusionsbizarreLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsnihilistic = models.BooleanField(default=False)

    delusionsnihilisticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    delusionsreligious = models.BooleanField(default=False)

    delusionsreligiouslevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Self Abuse

    selfAbuseNonreported = models.BooleanField(default=False)

    selfAbuseSelfMutilation = models.BooleanField(default=False)

    selfAbuseSelfMutilationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbuseSucidal = models.BooleanField(default=False)

    selfAbuseSucidalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbuseIntent = models.BooleanField(default=False)

    selfAbuseIntentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    selfAbusePlan = models.BooleanField(default=False)

    selfAbusePlanLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #other

    otherNoneReported = models.BooleanField(default= False)

    otherAutistic = models.BooleanField(default =False)

    otherAutisticLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherObsessional =models.BooleanField(default=False)

    otherObsessionalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPhobic = models.BooleanField(default=False)

    otherPhobicLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherGuilty = models.BooleanField(default=False)

    otherGuiltyLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherIdeasOfreference = models.BooleanField(default= False)

    otherIdeasOfreferenceLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES) 

    otherPreoccupied = models.BooleanField(default=False)

    otherPreoccupiedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherGuraded = models.BooleanField(default=False)

    otherGuradedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherOption = models.BooleanField(default=False)

    otherOptionText = models.CharField(max_length=1000)

    #Aggressive

    aggressiveNoneReported = models.BooleanField(default=False)

    aggressiveHomicidal = models.BooleanField(default=False)

    aggressiveHomicidalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    aggresiveIntent = models.BooleanField(default=False)

    aggresiveIntentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    aggressivePlan = models.BooleanField(default=False)

    aggressivePlanLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    
    
    #Perception/Hallucinations

    hallucinationsNoneReported = models.BooleanField(default= False)

    hallucinationsAuditory = models.BooleanField(default=False)

    hallucinationsAuditoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsVisual = models.BooleanField(default= False)

    hallucinationsVisualLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsOlfactory = models.BooleanField(default=False)

    hallucinationsOlfactoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsGustatory = models.BooleanField(default = False)

    hallucinationsGustatoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    hallucinationsTactile = models.BooleanField(default= False)

    hallucinationsTactileLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Other/Perception

    otherPerceptionNonreported = models.BooleanField(default= False)

    otherPerceptionIllusions = models.BooleanField(default =False)

    otherPerceptionIllusionsLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPerceptionDepersonalization = models.BooleanField(default=False)

    otherPerceptionDepersonalizationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    otherPerceptionDerealization = models.BooleanField(default=False)

    otherPerceptionDerealizationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Thought Process

    thoughtProcessLogical = models.BooleanField(default= False)
    
    thoughtProcessLogicalLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessCircumstantial = models.BooleanField(default = False)

    thoughtProcessCircumstantialLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessTangential = models.BooleanField(default= False)

    thoughtProcessTangentialLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessLoose = models.BooleanField(default=False)

    thoughtProcessLooseLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessRacing = models.BooleanField(default= False)

    thoughtProcessRacingLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessIncoherent = models.BooleanField(default= False)

    thoughtProcessIncoherentLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessConcrete = models.BooleanField(default= False)

    thoughtProcessConcreteLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessBlocked = models.BooleanField(default= False)

    thoughtProcessBlockedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    thoughtProcessFlightOfIdeas = models.BooleanField(default= False)

    thoughtProcessFlightOfIdeasLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #mood

    moodEuthymic = models.BooleanField(default= False)

    moodEuthymicLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodDepressed = models.BooleanField(default= False)

    moodDepressedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodAnxious = models.BooleanField(default= False)

    moodAnxiousLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodAngry = models.BooleanField(default= False)

    moodAngryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodEuphoric = models.BooleanField(default= False)
    
    moodEuphoricLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    moodIrritable = models.BooleanField(default= False)

    moodIrritableLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    #Affect

    affectFull = models.BooleanField(default= False)

    affectFullLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectConstricted = models.BooleanField(default= False)

    affectConstrictedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectFlat = models.BooleanField(default= False)

    affectFlatLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectInappropriate = models.BooleanField(default= False)

    affectInappropriateLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    affectLabile = models.BooleanField(default= False)

    affectLabileLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Behavior

    behaviorCooperative = models.BooleanField(default= False)

    behaviorCooperativelevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorResistant = models.BooleanField(default= False)

    behaviorResistantLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAgitated = models.BooleanField(default= False)

    behaviorAgitatedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorImpulsive = models.BooleanField(default= False)

    behaviorImpulsiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorOverSedated = models.BooleanField(default= False)

    behaviorOverSedatedLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    
    #
    behaviorAssaultive = models.BooleanField(default= False)

    behaviorAssaultiveLevels =models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAggresive = models.BooleanField(default= False)

    behaviorAggresiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorHyperactive = models.BooleanField(default= False)

    behaviorHyperactiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorRestless = models.BooleanField(default= False)

    behaviorRestlessLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorLossOfInterest = models.BooleanField(default= False)

    behaviorLossOfInterestLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)
    #
    behaviorAnhedonia = models.BooleanField(default= False)
    
    behaviorAnhedoniaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorAkasthisia = models.BooleanField(default= False)

    behaviorAkasthisiaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorWithdrawn = models.BooleanField(default= False)

    behaviorWithdrawnLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorDystonia = models.BooleanField(default= False)

    behaviorDystoniaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorTardive = models.BooleanField(default= False)

    behaviorTardiveLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    behaviorDyskinesia = models.BooleanField(default= False)

    behaviorDyskinesiaLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)


    #Cognition

    impairmentofNonReported = models.BooleanField(default= False)

    impairmentofOrientation = models.BooleanField(default= False)

    impairmentofOrientationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofMemory = models.BooleanField(default= False)

    impairmentofMemoryLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofAttentionConcentration = models.BooleanField(default= False)

    impairmentofAttentionConcentrationLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    impairmentofAbilityToAbstract = models.BooleanField(default= False)

    impairmentofAbilityToAbstractLevels = models.CharField(max_length=100, choices= SLOWEDCHOICES)

    #Intelligence

    IntelligenceMR = models.BooleanField(default= False)

    IntelligenceMRLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceBorderline = models.BooleanField(default= False)

    IntelligenceBorderlineLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceAverage = models.BooleanField(default= False)

    IntelligenceAverageLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)

    IntelligenceAboveAverage = models.BooleanField(default= False)

    IntelligenceAboveAverageLevels = models.CharField(max_length=100, choices=SLOWEDCHOICES)



    #Insight judgement 

    InsightjudgementNA = models.BooleanField(default= False)

    Insightjudgement = models.CharField(max_length=1000, default= '')


    elaborationOfPositiveMentalStatusNA= models.BooleanField(default=False)

    elaborationOfPositiveMentalStatus = models.CharField(max_length=1000)

    dsmVCodes = models.BooleanField(default=False)

    icd10codes = models.BooleanField(default = False)

        # ICD codes
     
    ICDCODES =(
        ('1','F31.73- Bipolar disorder, in partial remission, most recent episode manic'),
        ('2', 'F05	Delirium due to another medical condition'),
        ('3', 'F05	Delirium due to multiple etiologies'),
        ('4', 'F06.0	Psychotic disorder due to another medical condition, With hallucinations'),
        ('5', 'F06.1	Catatonia associated with another mental disorder (catatonia specifier)'),
        ('6', 'F06.1	Catatonic disorder due to another medical condition'),
        ('7','F07'),)
    
    #TODo

    icdcode = models.CharField(max_length=1000, choices=SLOWEDCHOICES)
    #DX

    dx = models.CharField(max_length=1000, default ='')

    dx1 = models.CharField(max_length=1000, default='')

    dx2 = models.CharField(max_length=1000, default='')

    dx3 = models.CharField(max_length=1000, default='')

    #CPT Code

    CPTCODES = (
        ('1', '99201 - Office_OP New Pat Initial minimum Cmplexity 10 mins'),
        ('2', '99202 - Office_OP New Pat Initial Low Compelexity 20 mins'),
        ('3', '99203 - Office_OP New Pat Initial Moderate Compelexity 30 mins'),
        ('4', '99204 - Office_OP New Pat Initial Comprehensive Compelexity 45 mins'),
        ('5', '99205 - Office_OP New Pat Initial High Compelexity 60 mins'),
        ('6', '99211 - Office_Op Est Pat Follow-Up Minimum Complex 5 mins'),
        ('7', '99212 - Office_Op Est Pat Follow-Up Low Complex 5 mins'),
        ('8', '99213 - Office _OP Est Pat Follow-Up Moderate COmplex 15 mins'),
        ('9', '99214 - Office_OP Est Follow Up Comprehensive Complex 25 mins'),
        ('10','99215 - Office_OP Est Pat Follow-Up High Complex 40 mins'),
        ('11', '99304 - Nursing New Pat Initial Low Complexity 25 mins'),
        ('12', '99305 - Nursing New Pat Initial Moderate Complexity 35 mins'),
        ('13', '99306 - Nursing New Pat Initial High Complexity 45 mins'),
        ('14', '99307 - Nursing Est pat Follow-Up Minimum Complex 10 mins'),
        ('15', '99308 - Nursing Est Pat Fllow-Up Low Complex 15 mins'),
        ('16', '99309 - Nursing Est Pat Follow-Up Moderate Complex 25 mins'),
        ('17', '99310 - Nursing Est Pat Follow-Up High Complex 35 mins'),
        ('18', '99318 - Nursing Est Pat Annual Assessment 60 mins'),
        ('19', '99341 - ALF New Pat New Patient Minimum Complex 15 mins'),
        ('20', '99342 - ALF New Pat New Patient Low Complex 30 mins'), 
        ('21', '99344 - ALF New Pat New Patint Moderate Complex 60 mins'),
        ('22', '99345 - ALF New Pat New Patent Comprehensive Comp. 75 mins'),
        ('23', '99417 - ALF New Pat add on for additional time past High 15 mins'),
        ('24', '99347 - ALF Est Pat Est Pt Min complex 20 mins'),
        ('25', '99348 - ALF Est Pat Est Pt Low COmplex 30 mins'),
        ('26', '99349 - ALF Est Pat Est Pt Moderate Complex 40 mins'),
        ('27', '99350 - ALf Est Pat Est Pt High Complex 60 mins'),
    )

    MODIFIERS = (
        ('1', 'GW - HOSPICE'),
        ('2', '95 - TELEHEALTH'),
    )
    cptcode1 = models.CharField(max_length=1000, choices=CPTCODES)

    cptcodeother1 = models.CharField(max_length= 1000, default = '')

    unit1 = models.CharField(max_length= 100, default= '')

    modifiers1 =models.CharField(max_length=100, choices=MODIFIERS)

    modifiers2 = models.CharField(max_length=100, choices=MODIFIERS)

    modifiersOther1 = models.CharField(max_length=1000, default ='')

    modifiersOther2 = models.CharField(max_length=1000, default ='')

    cptcode2 =  models.CharField(max_length=1000, choices=CPTCODES)

    cptcodeOther2 = models.CharField(max_length=1000, default='')

    unit2 = models.CharField(max_length=100, default = '')

    modefiers3 = models.CharField(max_length=100, choices=MODIFIERS)

    modefiers4 = models.CharField(max_length=100, choices=MODIFIERS)

    modefiersOther3 = models.CharField(max_length=1000, default ='')

    modefiersOther4 = models.CharField(max_length=1000, default ='')


    commentToBillers = models.TextField(max_length=10000, default='')

    commentMedical = models.TextField(max_length=10000, default='')

    commentMedicalNA = models.BooleanField(default=False)

    commentStressors = models.TextField(max_length=10000, default='')

    commentStressorsNA = models.BooleanField(default=False)

    #Radios

    RADIOCHOICES = (
        ('1', 'Yes'),
        ('2', 'No'),)
    radio1 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio2 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio3 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio4 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio5 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio6 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio7 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio8 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio9 = models.CharField(max_length=100, choices=RADIOCHOICES)

    radio1charField = models.CharField(max_length=100, default= '')

    radio2charField = models.CharField(max_length=100, default= '')

    radio3charField = models.CharField(max_length=100, default= '')

    radio4charField = models.CharField(max_length=100, default= '')

    radio5charField = models.CharField(max_length=100, default= '')

    radio6charField = models.CharField(max_length=100, default= '')

    radio7charField = models.CharField(max_length=100, default= '')

    radio8charField = models.CharField(max_length=100, default= '')

    radio9charField = models.CharField(max_length=100, default= '')





    #medication

    medicationsNonPrescribed = models.BooleanField(default=False)

    medicationName1 = models.CharField(max_length=100, default= '')

    medicationDosage1 = models.CharField(max_length=100, default= '')

    medicationAmount1 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue1 = models.CharField(max_length=100, default= '')

    rationale1 = models.CharField(max_length=100, default= '')


    medicationName2 = models.CharField(max_length=100, default= '')

    medicationDosage2 = models.CharField(max_length=100, default= '')

    medicationAmount2 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue2 = models.CharField(max_length=100, default= '')

    rationale2 = models.CharField(max_length=100, default= '')

    
    medicationName3 = models.CharField(max_length=100, default= '')

    medicationDosage3 = models.CharField(max_length=100, default= '')

    medicationAmount3 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue3 = models.CharField(max_length=100, default= '')

    rationale3 = models.CharField(max_length=100, default= '')


    medicationName4 = models.CharField(max_length=100, default= '')

    medicationDosage4 = models.CharField(max_length=100, default= '')

    medicationAmount4 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue4 = models.CharField(max_length=100, default= '')

    rationale4 = models.CharField(max_length=100, default= '')


    medicationName5 = models.CharField(max_length=100, default= '')

    medicationDosage5 = models.CharField(max_length=100, default= '')

    medicationAmount5 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue5 = models.CharField(max_length=100, default= '')

    rationale5 = models.CharField(max_length=100, default= '')
    

    medicationName6 = models.CharField(max_length=100, default= '')

    medicationDosage6 = models.CharField(max_length=100, default= '')

    medicationAmount6 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue6 = models.CharField(max_length=100, default= '')

    rationale6 = models.CharField(max_length=100, default= '')


    medicationName7 = models.CharField(max_length=100, default= '')

    medicationDosage7 = models.CharField(max_length=100, default= '')

    medicationAmount7 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue7 = models.CharField(max_length=100, default= '')

    rationale7 = models.CharField(max_length=100, default= '')


    medicationName8 = models.CharField(max_length=100, default= '')

    medicationDosage8 = models.CharField(max_length=100, default= '')

    medicationAmount8 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue8 = models.CharField(max_length=100, default= '')

    rationale8 = models.CharField(max_length=100, default= '')

    
    medicationName9 = models.CharField(max_length=100, default= '')

    medicationDosage9 = models.CharField(max_length=100, default= '')

    medicationAmount9 = models.CharField(max_length=100, default= '')

    medicationNewContinueDiscontinue9 = models.CharField(max_length=100, default= '')

    rationale9 = models.CharField(max_length=100, default= '')


    additionaCommentsOnMedicationsNA = models.BooleanField(default= False)

    additionaCommentsOnMedications = models.CharField(max_length=1000, default='')

    explainedRationaleForMedicalChoices = models.CharField(max_length=100, choices=RADIOCHOICES)

    explainedRationaleForMedicalcharfield = models.TextField(max_length=1000, default='')


    CLIENTOPTIONCHOICES =(
        ('1','Understands Information'),
        ('2', 'Does not understand'),
        ('3', 'Agrees with Medication'), 
        ('4', 'Refuses Medication')
    )
    #client/respond

    clientOptions = models.CharField(max_length=100, choices=CLIENTOPTIONCHOICES)

    guardianOptions = models.CharField(max_length=100, choices=CLIENTOPTIONCHOICES)

    
    #laboratory Tests Check Boxes
    laboratoryTestsNoneOrdered = models.BooleanField(default=False)

    laboratoryTestsCBC = models.BooleanField(default=False)

    laboratoryTestsHepaticpanel =models.BooleanField(default=False)

    laboratoryTestsTSH = models.BooleanField(default=False)

    laboratoryTestsLibidProfile = models.BooleanField(default=False)

    laboratoryTestsCMP = models.BooleanField(default=False)

    laboratoryTestsOther =models.BooleanField(default=False)


    #followup Plan

    followupPlan1 = models.CharField(max_length=500, default='')

    followupPlan2 = models.CharField(max_length=500, default= '')

    followupPlan3 = models.CharField(max_length=500, default= '')

    followupPlan4 = models.CharField(max_length=500, default= '')

    followupPlan5 = models.CharField(max_length=500, default= '')


    #other considerations

    otherConsiderationsNone = models.BooleanField(default=False)

    otherConsiderations = models.TextField(max_length=1000)

    #Date Of Service

    dateofService = models.CharField(max_length=100, default='')

    staffIDNo = models.CharField(max_length=1000 , default='')

    locCode = models.CharField(max_length=1000, default='')

    prcdrCode = models.CharField(max_length=1000, default='')

    mod1 = models.CharField(max_length=1000, default='')

    mod2 = models.CharField(max_length=1000, default='')

    mod3 = models.CharField(max_length=1000, default='')

    mod4 = models.CharField(max_length=1000, default= '')

    startTime = models.CharField(max_length=1000, default='')

    stopTime = models.CharField(max_length=1000, default='')

    totalTime = models.CharField(max_length=1000, default='')

    diagnosticCode = models.CharField(max_length=1000, default='')

    
class PsychiatricProgessNote(models.Model):
    
    LETTER_HEAD_CHOICES =(
            ('1','CHILD NET'),
            ('2','DYNAMIC HEADER'),
        )
    
    APPOINTMENTMODE = (
        ('1', 'Telehealth only-Consent obtained'),
        ('2', 'Audio/Video'),
        ('3','Audio Only-Ph number'),
    )
    POSCHOICES = (

        ('1', '02 - TELEHEALTH'),
        ('2', '04 - HOMELESS SHELTER'),
        ('3', '10 - HOME'),
        ('4', '11 - OFFICE'),
        ('5', '13 - ASSISTED LIVING FACILITY'),
        ('6', '21 - INPATIENT HOSPITAL'),
        ('7', '22 - OUTPATIENT HOSPITAL'),
        ('8', '23 - EMERGENCY ROOM HOSPITAL'),
        ('9', '24 - AMBULATORY SURGICAL CENTER'),
        ('10', '25 - BIRTHING CENTER'),
        ('11', '26 - MILITARY TREATMENT FACILITY'),
        ('12', '31 - SKILLED NURSING FACILITY'),
    )

    APPOINTMENTTYPE = (
        ('1', 'Assessment'),
        ('2', 'Medication Review'),
        ('3', 'Therapy'),
    )
    letterhead = models.CharField(max_length=1000,choices=LETTER_HEAD_CHOICES, default='')

    clientName = models.CharField(max_length=1000, default = '')

    appointmentDate = models.DateField()
    
    pos = models.CharField(max_length=1000, choices=POSCHOICES)

    appointmentMode= models.CharField(max_length=1000, choices=APPOINTMENTMODE)

    appointmenttype = models.CharField(max_length=1000, choices=APPOINTMENTTYPE)

    dateOfNextPlan= models.DateField()

    timeStart = models.CharField(max_length=100, default='')

    timeEnd = models.CharField(max_length=100, default='')

    statementOfProgress = models.CharField(max_length=1000, default='')

    currentMedicationPrescribedNA = models.BooleanField(default=False)

    currentMedicationPrescribed = models.CharField(max_length=1000, default='')

    documentationOfChangesNA = models.CharField(max_length=100, default=False)

    documentationOfChanges = models.CharField(max_length=1000, default='')

    issuesNeedingtobeaddressedNA = models.BooleanField(max_length=100, default=False)

    issuesNeedingtobeaddressed = models.CharField(max_length=1000, default='')

    labStudiesOrdered = models.BooleanField(max_length=100, default=False)

    medicationEducationNA = models.BooleanField(max_length=100,default=False)

    medicationEducation = models.CharField(max_length=1000, default ='')

    atypicalmedication = models.BooleanField(max_length=100, default=False)

    #Appearance

    appearanceWellGroomed = models.BooleanField(default=False)

    appearanceUnkempt = models.BooleanField(default=False)

    appearanceBizarreCombinations = models.BooleanField(default=False)

    appearanceUnableToAssessAppointmentDoneViaPhone = models.BooleanField(default=False)

    behaviorCooperative = models.BooleanField(default=False)

    behaviorThreatening = models.BooleanField(default=False)

    behaviorSuspicious = models.BooleanField(default= False)

    behaviorUncooperative = models.BooleanField(default=False)

    behaviorHyperactive = models.BooleanField(default=False)

    behaviorPooeAttention = models.BooleanField(default=False)

    speechNormal = models.BooleanField(default=False)

    speechSlow = models.BooleanField(default=False)

    speechPressured = models.BooleanField(default=False)

    speechLoud = models.BooleanField(default=False)

    speechSoft = models.BooleanField(default=False)

    speechRambling = models.BooleanField(default=False)

    speechIncoherent = models.BooleanField(default=False)

    moodNormal =models.BooleanField(default=False)

    moodDepressed = models.BooleanField(default=False)

    moodAnxious = models.BooleanField(default=False)

    moodAngry = models.BooleanField(default=False)

    moodElated = models.BooleanField(default=False)

    moodIrritable = models.BooleanField(default=False)

    affectAppropriate = models.BooleanField(default=False)

    affectFull = models.BooleanField(default=False)

    affectInappropriate = models.BooleanField(default=False)

    affectConstricted = models.BooleanField(default=False)

    affectBlunted = models.BooleanField(default=False)

    affectFlat = models.BooleanField(default=False)

    affectLabile = models.BooleanField(default = False)

    thoughtGoalDirected = models.BooleanField(default=False)

    thoughtDelusions = models.BooleanField(default= False)

    thoughtLogical = models.BooleanField(default=False)

    thoughtCircumstantial = models.BooleanField(default=False)

    thoughtObsessions = models.BooleanField(default=False)

    thoughtConcrete = models.BooleanField(default =False)

    thoughtLoose = models.BooleanField(default=False)

    thoughtHallucination = models.BooleanField(default=False)

    ideationSuicidal = models.BooleanField(default = False)

    ideationDenies = models.BooleanField(default=False)

    ideationSuicidalifPresentDescibe =models.CharField(max_length=1000, default='')

    ideationHomocidal = models.BooleanField(default=False)

    ideationDenies2 = models.BooleanField(default=False)

    ideationHomicidalPresentDescribe = models.CharField(max_length=1000, default='')

    ideation1Week = models.BooleanField(default=False)

    ideation2week = models.BooleanField(default=False)

    ideation4weeks = models.BooleanField(default=False)

    ideation1month = models.BooleanField(default=False)

    ideation2months =models.BooleanField(default=False)

    ideation3monts = models.BooleanField(default=False)

    ideationother = models.BooleanField(default=False)

    
    
    ICDCODES =(
        ('1','F31.73- Bipolar disorder, in partial remission, most recent episode manic'),
        ('2', 'F05	Delirium due to another medical condition'),
        ('3', 'F05	Delirium due to multiple etiologies'),
        ('4', 'F06.0	Psychotic disorder due to another medical condition, With hallucinations'),
        ('5', 'F06.1	Catatonia associated with another mental disorder (catatonia specifier)'),
        ('6', 'F06.1	Catatonic disorder due to another medical condition'),
        ('7','F07'),)
    
    mentalRetardation =(
        ('1','Problems with primary support group - Becoming a parent'),
        ('2', 'Problems with primary support group - birth with sibiling'),
        ('3', 'Problems with primary support group - Death of a family member'),
        ('4', 'Problems with primary support group - Discord'),
        ('5', 'Problems with primary support group - Discord with siblings'),
        ('6', 'Problems with primary support group - Disruption of family by separation, divorce or estrangement'),
        ('7', 'Problems with primary support group - Engagement'),
        ('8', 'Problems with primary support group - Friction with child'),
        ('9', 'Problems with primary support group - Health problems in family'),
        ('10','Problems with primary support group - Illness of child'),
        ('11', 'Problems with primary support group - Inadequate dicipline'),
        ('12', 'Problems with primary suppoet group - Long term mental illness'),
        ('13', 'Problems with primary support group - Marriage'),
        ('14', 'Problems with primary support group - Neglect of child'),
        ('15', 'Problems with primary support group - Parental Overprotection'),
        ('16', 'Problems with primary support group - Personal Physical illness or injury'),
        ('17', 'Problems with primary support group - Sexual or Physical abuse'),
        ('18', 'Problems with social related environment - Adjustment to life cycle transition'),
        ('19', 'Problems related to social environment - Death or losst of friend'),
        ('20', 'Problems related to social environment - Difficulties with interpersonal relationship'),
        ('21', 'Problems related to social environment - Difficulty with acculturation'),
        ('22', 'Problems related to social environment - Discrimination'),
        ('23', 'Problems related to social environment - Illness of best friend'),
        ('24', 'Problems related to social environment - Inadequate social support'),
        ('25', 'Problems related to social environment - Living alone'),
        ('26', 'Educational Problems- Academic problems'),
        ('27', 'Educational Problems - Discord with teachers or classmates'),
        ('28', 'Educational Problems - Illiteracy'),
        ('29', 'Educational Problems - School problems'),
        ('30', 'Occupational Problems - Difficult work condition'),
        ('31', 'Occupational Problems - Discord with boss or coworkers'),
        ('32', 'Occupational Problems - Homemaking'),
        ('33', 'Occupational Problems - Job change'),
        ('34', 'Occupational Problems - Job dissatisfaction'),
        ('35', 'Occupational Problems - Stressful work schedule'),
        ('36', 'Occupational Problems - Threat of job loss'),
        ('37', 'Occupational Problems - Unemployment'),
        ('38', 'Housing problems - Change in residence'),
        ('39', 'Housing problems - Discord with neighbors or landlords'),
        ('40', 'Housing problems - Homelessness'),
        ('41', 'Housing problems - immigration'),
        ('42', 'Housing problems - Inadequate housing'),
        ('43', 'Housing problems - Threat to personal safety'),
        ('44', 'Housing problems - Unsafe neighborhood'))
    
    
    #TODo

    icdcode = models.CharField(max_length=1000, choices=ICDCODES  )
    #DX

    otherICDCode = models.CharField(max_length=1000, choices=ICDCODES)

    generalMedicalConditions = models.CharField(max_length=1000, default='')

    personalityDisorderMentalRetardation = models.CharField(max_length=1000, choices=mentalRetardation)

    otherpersonalDiagnosis = models.CharField(max_length=1000, default = '')



    #CPT Code

    CPTCODES = (
        ('1', '99201 - Office_OP New Pat Initial minimum Cmplexity 10 mins'),
        ('2', '99202 - Office_OP New Pat Initial Low Compelexity 20 mins'),
        ('3', '99203 - Office_OP New Pat Initial Moderate Compelexity 30 mins'),
        ('4', '99204 - Office_OP New Pat Initial Comprehensive Compelexity 45 mins'),
        ('5', '99205 - Office_OP New Pat Initial High Compelexity 60 mins'),
        ('6', '99211 - Office_Op Est Pat Follow-Up Minimum Complex 5 mins'),
        ('7', '99212 - Office_Op Est Pat Follow-Up Low Complex 5 mins'),
        ('8', '99213 - Office _OP Est Pat Follow-Up Moderate COmplex 15 mins'),
        ('9', '99214 - Office_OP Est Follow Up Comprehensive Complex 25 mins'),
        ('10','99215 - Office_OP Est Pat Follow-Up High Complex 40 mins'),
        ('11', '99304 - Nursing New Pat Initial Low Complexity 25 mins'),
        ('12', '99305 - Nursing New Pat Initial Moderate Complexity 35 mins'),
        ('13', '99306 - Nursing New Pat Initial High Complexity 45 mins'),
        ('14', '99307 - Nursing Est pat Follow-Up Minimum Complex 10 mins'),
        ('15', '99308 - Nursing Est Pat Fllow-Up Low Complex 15 mins'),
        ('16', '99309 - Nursing Est Pat Follow-Up Moderate Complex 25 mins'),
        ('17', '99310 - Nursing Est Pat Follow-Up High Complex 35 mins'),
        ('18', '99318 - Nursing Est Pat Annual Assessment 60 mins'),
        ('19', '99341 - ALF New Pat New Patient Minimum Complex 15 mins'),
        ('20', '99342 - ALF New Pat New Patient Low Complex 30 mins'), 
        ('21', '99344 - ALF New Pat New Patint Moderate Complex 60 mins'),
        ('22', '99345 - ALF New Pat New Patent Comprehensive Comp. 75 mins'),
        ('23', '99417 - ALF New Pat add on for additional time past High 15 mins'),
        ('24', '99347 - ALF Est Pat Est Pt Min complex 20 mins'),
        ('25', '99348 - ALF Est Pat Est Pt Low COmplex 30 mins'),
        ('26', '99349 - ALF Est Pat Est Pt Moderate Complex 40 mins'),
        ('27', '99350 - ALf Est Pat Est Pt High Complex 60 mins'),
    )

    MODIFIERS = (
        ('1', 'GW - HOSPICE'),
        ('2', '95 - TELEHEALTH'),
    )
    cptcode1 = models.CharField(max_length=1000, choices=CPTCODES)

    cptcodeother1 = models.CharField(max_length= 1000, default = '')

    unit1 = models.CharField(max_length= 100, default= '')

    modifiers1 =models.CharField(max_length=100, choices=MODIFIERS)

    modifiers2 = models.CharField(max_length=100, choices=MODIFIERS)

    modifiersOther1 = models.CharField(max_length=1000, default ='')

    modifiersOther2 = models.CharField(max_length=1000, default ='')

    cptcode2 =  models.CharField(max_length=1000, choices=CPTCODES)

    cptcodeOther2 = models.CharField(max_length=1000, default='')

    unit2 = models.CharField(max_length=100, default = '')

    modefiers3 = models.CharField(max_length=100, choices=MODIFIERS)

    modefiers4 = models.CharField(max_length=100, choices=MODIFIERS)

    modefiersOther3 = models.CharField(max_length=1000, default ='')

    modefiersOther4 = models.CharField(max_length=1000, default ='')








    







    

    
















































































    

























        















    












