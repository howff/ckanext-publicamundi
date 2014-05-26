# -*- coding: utf-8 -*-

languages = [{'display': 'Greek', 'value': 'el'}, {'display': 'English', 'value': 'en'}, {'display': 'Italian', 'value': 'it'}, {'display': 'Irish', 'value': 'ga'}, {'display': 'Czech', 'value': 'cs'}, {'display': 'Estonian', 'value': 'et'}, {'display': 'Spanish', 'value': 'es'}, {'display': 'Dutch', 'value': 'nl'}, {'display': 'Portuguese', 'value': 'pt'}, {'display': 'Latvian', 'value': 'lv'}, {'display': 'Lithuanian', 'value': 'lt'}, {'display': 'Romanian', 'value': 'ro'}, {'display': 'Polish', 'value': 'pl'}, {'display': 'French', 'value': 'fr'}, {'display': 'Bulgarian', 'value': 'bg'}, {'display': 'German', 'value': 'de'}, {'display': 'Danish', 'value': 'da'}, {'display': 'Finnish', 'value': 'fi'}, {'display': 'Hungarian', 'value': 'hu'}, {'display': 'Swedish', 'value': 'sv'}, {'display': 'Slovak', 'value': 'sk'}, {'display': 'Maltese', 'value': 'mt'}, {'display': 'Slovenian', 'value': 'sl'}]


topic_category = [{'display': 'IntelligenceMilitary', 'display-el': "Στρατιωτικές πληροφορίες",'value': 'intelligencemilitary'}, 
		{'display': 'Environment', 'display-el':"Περιβάλλον", 'value': 'environment'}, 
		{'display': 'GeoscientificInformation', 'display-el':"Γεωεπιστημονικές πληροφορίες",'value': 'geoscientificinformation'}, 
		{'display': 'Elevation', 'display-el':"Υψομετρία",'value': 'elevation'}, 
		{'display': 'UtilitiesCommunication', 'display-el':"Επιχειρήσεις κοινής ωφελείας/Επικοινωνία", 'value': 'utilitiescommunication'}, 
		{'display': 'Structure', 'display-el':"Κατασκευές",'value': 'structure'}, 
		{'display': 'Oceans', 'display-el':"Θάλασσες",'value': 'oceans'}, 
		{'display': 'PlanningCadastre', 'display-el':"Χωροταξία/Κτηματολόγιο",'value': 'planningcadastre'}, 
		{'display': 'InlandWaters', 'display-el':"Εσωτερικά ύδατα", 'value': 'inlandwaters'}, 
		{'display': 'Boundaries', 'display-el':"Όρια",'value': 'boundaries'}, 
		{'display': 'Society', 'display-el':"Κοινωνία",'value': 'society'}, 
		{'display': 'Biota', 'display-el':"Βιόκοσμος",'value': 'biota'}, 
		{'display': 'Health', 'display-el':"Υγεία", 'value': 'health'}, 
		{'display': 'Location', 'display-el':"Γεωγραφική θέση", 'value': 'location'}, 
		{'display': 'ClimatologyMeteorologyAtmosphere', 'display-el':"Κλιματολογία/Μετεωρολογία/Ατμόσφαιρα",'value': 'climatologymeteorologyatmosphere'}, 
		{'display': 'Transportation', 'display-el':"Μεταφορές", 'value': 'transportation'}, 
		{'display': 'Farming', 'display-el':"Γεωργία",'value': 'farming'}, 
		{'display': 'ImageryBaseMapsEarthCover', 'display-el':"Ορθοεικόνες/Βασικοί χάρτες/Κάλυψη γης",'value': 'imagerybasemapsearthcover'}, 
		{'display': 'Economy', 'display-el':"Οικονομία",'value': 'economy'}]

countries = [{'display': 'Belgium', 'value': 'BE'}, 
		{'display': 'France', 'value': 'FR'}, 
		{'display': 'Bulgaria', 'value': 'BG'}, 
		{'display': 'Bosnia and Herzegovina', 'value': 'BA'}, 
		{'display': 'Saint-Berthelemy', 'value': 'BL'}, 
		{'display': 'Spain Continental', 'value': 'ESCO'}, 
		{'display': 'Reunion', 'value': 'REU'}, 
		{'display': 'Finland', 'value': 'FI'}, 
		{'display': 'Belarus', 'value': 'BY'}, 
		{'display': 'Denmark', 'value': 'DK'}, 
		{'display': 'Russian Federation', 'value': 'RU'}, 
		{'display': 'Netherlands', 'value': 'NL'}, 
		{'display': 'Norway', 'value': 'NO'}, 
		{'display': 'World', 'value': 'WO'}, 
		{'display': 'Romania', 'value': 'RO'}, 
		{'display': 'Switzerland', 'value': 'CH'}, 
		{'display': 'Greece', 'value': 'GR'}, 
		{'display': 'Guadeloupe', 'value': 'GP'}, 
		{'display': 'EU-12', 'value': 'EU12'}, 
		{'display': 'EU-15', 'value': 'EU15'}, 
		{'display': 'Czech Republic', 'value': 'CZ'}, 
		{'display': 'Azores', 'value': 'AZ'}, 
		{'display': 'United Kingdom', 'value': 'GB'}, 
		{'display': 'Gibraltar', 'value': 'GI'}, 
		{'display': 'Slovakia', 'value': 'SK'}, 
		{'display': 'Slovenia', 'value': 'SI'}, 	
		{'display': 'San Marino', 'value': 'SM'}, 
		{'display': 'Sweden', 'value': 'SE'}, 
		{'display': 'EU-25', 'value': 'EU25'}, 
		{'display': 'Portugal Continental', 'value': 'PTCO'}, 
		{'display': 'EU-27', 'value': 'EU27'}, 
		{'display': 'Croatia', 'value': 'HR'}, 
		{'display': 'Germany', 'value': 'DE'}, 
		{'display': 'Hungary', 'value': 'HU'}, 
		{'display': 'Canaries', 'value': 'CAN'}, 
		{'display': 'Madeira', 'value': 'MADE'}, 
		{'display': 'Portugal', 'value': 'PT'}, 
		{'display': 'Turkey', 'value': 'TR'}, 
		{'display': 'Liechtenstein', 'value': 'LI'}, 
		{'display': 'Latvia', 'value': 'LV'}, 
		{'display': 'Lithuania', 'value': 'LT'}, 
		{'display': 'Luxembourg', 'value': 'LU'}, 
		{'display': 'Poland', 'value': 'PL'}, 
		{'display': 'Holy See Vatican City State', 'value': 'VA'}, 
		{'display': 'France Continental', 'value': 'FRCO'}, 
		{'display': 'Andorra', 'value': 'AD'}, 
		{'display': 'Estonia', 'value': 'EE'}, 
		{'display': 'Albania', 'value': 'AL'}, 
		{'display': 'Italy', 'value': 'IT'}, 
		{'display': 'Isle of Man', 'value': 'IM'}, 
		{'display': 'Austria', 'value': 'AT'}, 
		{'display': 'Ireland', 'value': 'IE'}, 
		{'display': 'Spain', 'value': 'ES'}, 
		{'display': 'Moldova', 'value': 'MD'},
		{'display': 'Saint-Martin', 'value': 'MF'}, 
		{'display': 'Morocco', 'value': 'MA'}, 
		{'display': 'French Guiana', 'value': 'GF'}, 
		{'display': 'Cyprus', 'value': 'CY'}, 
		{'display': 'Former Yugoslav Republic of Macedonia', 'value': 'MK'}, 
		{'display': 'Malta', 'value': 'MT'}, 
		{'display': 'Martinique', 'value': 'MQ'}, 
		{'display': 'Ukraine', 'value': 'UA'}]

date_types = [
            {'value':"creation", 'display':"Date of Creation", 'display-el':"Ημερομηνία δημιουργίας"},
            {'value':"publication", 'display':"Publication Date", 'display-el': "Ημερομηνία δημοσίευσης"},
            {'value':"revision", 'display':"Last revision Date", 'display-el': "Ημερομηνία τελευταίας αναθεώρησης"}]

degrees = [{'display': 'Not evaluated', 'value': 'not_evaluated'}, {'display': 'Conformant', 'value': 'conformant'}, {'display': 'Not conformant', 'value': 'not_conformant'}]



party_roles = [{'display': 'Originator', 'display-el':"Δημιουργός",'value': 'originator'}, 
		{'display': 'PointOfContact','display-el':"Αρμόδιος για επικοινωνία", 'value': 'pointofcontact'}, 
		{'display': 'Custodian', 'display-el':"Υπόλογος", 'value': 'custodian'}, 
		{'display': 'ResourceProvider','display-el':"Πάροχος πόρου", 'value': 'resourceprovider'}, 
		{'display': 'Owner', 'display-el':"Κάτοχος", 'value': 'owner'}, 
		{'display': 'User', 'display-el':"Χρήστης", 'value': 'user'}, 
		{'display': 'Distributor','display-el':"Διανομέας",  'value': 'distributor'}, 
		{'display': 'Publisher', 'display-el':"Εκδότης",  'value': 'publisher'}, 
		{'display': 'PrincipalInvestigator', 'display-el':"Πρωτεύων διερευνητής", 'value': 'investigator'}, 
		{'display': 'Author','display-el': "Συντάκτης", 'value': 'author'}, 
		{'display': 'Processor', 'display-el':"Επεξεργαστής", 'value': 'processor'}]



inspire_data_themes_gr = [
            "Έδαφος",
            "Ανθρώπινη υγεία και ασφάλεια",
            "Ατμοσφαιρικές συνθήκες",
            "Βιογεωγραφικές περιοχές",
            "Γεωλογία",
            "Γεωργικές εγκαταστάσεις και εγκαταστάσεις υδατοκαλλιέργειας",
            "Γεωτεμάχια κτηματολογίου",
            "Δίκτυα μεταφορών",
            "Διευθύνσεις",
            "Διοικητικές ενότητες",
            "Εγκαταστάσεις παραγωγής και βιομηχανικές εγκαταστάσεις",
            "Εγκαταστάσεις παρακολούθησης του περιβάλλοντος",
            "Ενδιαιτήματα και βιότοποι",
            "Ενεργειακοί πόροι",
            "Επιχειρήσεις κοινής ωφελείας και κρατικές υπηρεσίες",
            "Ζώνες διαχείρισης/περιορισμού/ρύθμισης εκτάσεων και μονάδες αναφοράς",
            "Ζώνες φυσικών κινδύνων",
            "Θαλάσσιες περιοχές",
            "Κάλυψη γης",
            "Κατανομή ειδών",
            "Κατανομή πληθυσμού - δημογραφία",
            "Κτίρια",
            "Μετεωρολογικά γεωγραφικά χαρακτηριστικά",
            "Ορθοφωτογραφία",
            "Ορυκτοί πόροι",
            "Προστατευόμενες τοποθεσίες",
            "Στατιστικές μονάδες",
            "Συστήματα γεωγραφικού καννάβου",
            "Συστήματα συντεταγμένων",
            "Τοπωνύμια",
            "Υδρογραφία",
            "Υψομετρία",
            "Χρήσεις γης",
            "Ωκεανογραφικά γεωγραφικά χαρακτηριστικά"]













