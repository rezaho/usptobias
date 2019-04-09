from google.cloud import bigquery

INT = 'INTEGER'
STR = 'STRING'
BOO = 'BOOLEAN'
FLO = 'FLOAT'
DAT = 'DATE'
GEO = 'GEOGRAPHY'

NULL = 'NULLABLE'
REQ = 'REQUIRED'


class Schema:
    """
    This class contains the schema of PatStat2016a tables
    TODO: CHECK SCHEMA
    """

    def __init__(self):
        self.tls201 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_auth', STR, NULL, None, ()),
            bigquery.SchemaField('appln_nr', STR, NULL, None, ()),  # detected as FLOAT
            bigquery.SchemaField('appln_kind', STR, NULL, None, ()),
            bigquery.SchemaField('appln_filing_date', DAT, NULL, None, ()),
            bigquery.SchemaField('appln_filing_year', INT, NULL, None, ()),
            bigquery.SchemaField('appln_nr_epodoc', STR, NULL, None, ()),
            bigquery.SchemaField('appln_nr_original', STR, NULL, None, ()),  # detected as FLOAT
            bigquery.SchemaField('ipr_type', STR, NULL, None, ()),
            bigquery.SchemaField('receiving_office', STR, NULL, None, ()),
            bigquery.SchemaField('internat_appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('int_phase', BOO, NULL, None, ()),
            bigquery.SchemaField('reg_phase', BOO, NULL, None, ()),
            bigquery.SchemaField('nat_phase', BOO, NULL, None, ()),  # detected as STRING
            bigquery.SchemaField('earliest_filing_date', DAT, NULL, None, ()),
            bigquery.SchemaField('earliest_filing_year', INT, NULL, None, ()),
            bigquery.SchemaField('earliest_filing_id', INT, NULL, None, ()),
            bigquery.SchemaField('earliest_publn_date', DAT, NULL, None, ()),
            bigquery.SchemaField('earliest_publn_year', INT, NULL, None, ()),
            bigquery.SchemaField('earliest_pat_publn_id', INT, NULL, None, ()),
            bigquery.SchemaField('granted', BOO, NULL, None, ()),  # detected as STRING
            bigquery.SchemaField('docdb_family_id', INT, NULL, None, ()),
            bigquery.SchemaField('inpadoc_family_id', INT, NULL, None, ()),
            bigquery.SchemaField('docdb_family_size', INT, NULL, None, ()),
            bigquery.SchemaField('nb_citing_docdb_fam', INT, NULL, None, ()),
            bigquery.SchemaField('nb_applicants', INT, NULL, None, ()),
            bigquery.SchemaField('nb_inventors', INT, NULL, None, ())
        ]
        
        self.tls202 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_title_lg', STR, NULL, None, ()),
            bigquery.SchemaField('appln_title', STR, NULL, None, ()),
        ]
        
        self.tls203 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_abstract_lg', STR, NULL, None, ()),
            bigquery.SchemaField('appln_abstract', STR, NULL, None, ())
        ]
        
        self.tls204 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('prior_appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('prior_appln_seq_nr', INT, NULL, None, ())
        ]
        
        self.tls205 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('tech_rel_appln_id', INT, NULL, None, ())
        ]
        
        self.tls206 = [
            bigquery.SchemaField('person_id', INT, REQ, None, ()),
            bigquery.SchemaField('person_name', STR, NULL, None, ()),
            bigquery.SchemaField('person_address', STR, NULL, None, ()),
            bigquery.SchemaField('person_ctry_code', STR, NULL, None, ()),
            bigquery.SchemaField('doc_std_name_id', INT, NULL, None, ()),
            bigquery.SchemaField('doc_std_name', STR, NULL, None, ()),
            bigquery.SchemaField('psn_id', INT, NULL, None, ()),  # check STR
            bigquery.SchemaField('psn_name', STR, NULL, None, ()),
            bigquery.SchemaField('psn_level', INT, NULL, None, ()),  # check STR
            bigquery.SchemaField('psn_sector', STR, NULL, None, ()),  # check STR
            # bigquery.SchemaField('han_id', INT, NULL, None, ()),  # check STR
            # bigquery.SchemaField('han_name', STR, NULL, None, ()),
            # bigquery.SchemaField('han_harmonized', STR, NULL, None, ())
        ]
        
        self.tls207 = [
            bigquery.SchemaField('person_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('applt_seq_nr', INT, NULL, None, ()),
            bigquery.SchemaField('invt_seq_nr', INT, NULL, None, ())
        ]

        self.tls209 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('ipc_class_symbol', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_class_level', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_version', DAT, NULL, None, ()),
            bigquery.SchemaField('ipc_value', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_position', STR, NULL, None, ()),
            bigquery.SchemaField('ipc_gener_auth', STR, NULL, None, ())
        ]
        
        self.tls210 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('nat_class_symbol', STR, NULL, None, ())
        ]
        
        self.tls211 = [
            bigquery.SchemaField('pat_publn_id', INT, REQ, None, ()),
            bigquery.SchemaField('publn_auth', STR, NULL, None, ()),
            bigquery.SchemaField('publn_nr', STR, NULL, None, ()),
            bigquery.SchemaField('publn_nr_original', STR, NULL, None, ()),
            bigquery.SchemaField('publn_kind', STR, NULL, None, ()),
            bigquery.SchemaField('appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('publn_date', DAT, NULL, None, ()),
            bigquery.SchemaField('publn_lg', STR, NULL, None, ()),
            bigquery.SchemaField('publn_first_grant', STR, NULL, None, ()),
            bigquery.SchemaField('publn_claims', INT, NULL, None, ()),
        ]
        self.tls212 = [
            bigquery.SchemaField('pat_publn_id', INT, REQ, None, ()),
            bigquery.SchemaField('citn_replenished', INT, NULL, None, ()),
            bigquery.SchemaField('citn_id', INT, NULL, None, ()),
            bigquery.SchemaField('citn_origin', STR, NULL, None, ()),
            bigquery.SchemaField('cited_pat_publn_id', INT, NULL, None, ()),
            bigquery.SchemaField('cited_appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('pat_citn_seq_nr', INT, NULL, None, ()),
            bigquery.SchemaField('cited_npl_publn_id', INT, NULL, None, ()),
            bigquery.SchemaField('npl_citn_seq_nr', INT, NULL, None, ()),
            bigquery.SchemaField('citn_gener_auth', STR, NULL, None, ()),
        ]
        
        self.tls214 = [
            bigquery.SchemaField('npl_publn_id', INT, REQ, None, ()),
            bigquery.SchemaField('npl_type', STR, NULL, None, ()),
            bigquery.SchemaField('npl_biblio', STR, NULL, None, ()),
            bigquery.SchemaField('npl_author', STR, NULL, None, ()),
            bigquery.SchemaField('npl_title1', STR, NULL, None, ()),
            bigquery.SchemaField('npl_title2', STR, NULL, None, ()),
            bigquery.SchemaField('npl_editor', STR, NULL, None, ()),
            bigquery.SchemaField('npl_volume', STR, NULL, None, ()),
            bigquery.SchemaField('npl_issue', STR, NULL, None, ()),
            bigquery.SchemaField('npl_publn_date', STR, NULL, None, ()),
            bigquery.SchemaField('npl_publn_end_date', STR, NULL, None, ()),
            bigquery.SchemaField('npl_publisher', STR, NULL, None, ()),
            bigquery.SchemaField('npl_page_first', STR, NULL, None, ()),
            bigquery.SchemaField('npl_page_last', STR, NULL, None, ()),
            bigquery.SchemaField('npl_abstract_nr', STR, NULL, None, ()),
            bigquery.SchemaField('npl_doi', STR, NULL, None, ()),
            bigquery.SchemaField('npl_isbn', STR, NULL, None, ()),
            bigquery.SchemaField('npl_issn', STR, NULL, None, ()),
            bigquery.SchemaField('online_availability', STR, NULL, None, ()),
            bigquery.SchemaField('online_classification', STR, NULL, None, ()),
            bigquery.SchemaField('online_search_date', STR, NULL, None, ())
        ]
        
        self.tls215 = [	
            bigquery.SchemaField('pat_publn_id', INT, REQ, None, ()),
            bigquery.SchemaField('citn_replenished', INT, NULL, None, ()),
            bigquery.SchemaField('citn_id', INT, NULL, None, ()),
            bigquery.SchemaField('citn_categ', STR, NULL, None, ())
        ]
        
        self.tls216 = [ 
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('parent_appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('contn_type', STR, NULL, None, ())
        ]
        
        self.tls222 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('jp_class_scheme', STR, NULL, None, ()),
            bigquery.SchemaField('jp_class_symbol', STR, NULL, None, ())
        ]
        
        self.tls223 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('docus_class_symbol', STR, NULL, None, ())
        ]
        
        self.tls224 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('cpc_class_symbol', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_scheme', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_version', DAT, NULL, None, ()),
            bigquery.SchemaField('cpc_value', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_position', STR, NULL, None, ()),
            bigquery.SchemaField('cpc_gener_auth', STR, NULL, None, ()),
        ]
        
        self.tls226 = [
            bigquery.SchemaField('person_orig_id', INT, REQ, None, ()),
            bigquery.SchemaField('person_id', INT, NULL, None, ()),
            bigquery.SchemaField('source', STR, NULL, None, ()),
            bigquery.SchemaField('source_version', STR, NULL, None, ()),
            bigquery.SchemaField('name_freeform', STR, NULL, None, ()),
            bigquery.SchemaField('last_name', STR, NULL, None, ()),
            bigquery.SchemaField('first_name', STR, NULL, None, ()),
            bigquery.SchemaField('middle_name', STR, NULL, None, ()),
            bigquery.SchemaField('address_freeform', STR, NULL, None, ()),
            bigquery.SchemaField('address_1', STR, NULL, None, ()),
            bigquery.SchemaField('address_2', STR, NULL, None, ()),
            bigquery.SchemaField('address_3', STR, NULL, None, ()),
            bigquery.SchemaField('address_4', STR, NULL, None, ()),
            bigquery.SchemaField('address_5', STR, NULL, None, ()),
            bigquery.SchemaField('street', STR, NULL, None, ()),
            bigquery.SchemaField('city', STR, NULL, None, ()),
            bigquery.SchemaField('zip_code', STR, NULL, None, ()),
            bigquery.SchemaField('state', STR, NULL, None, ()),
            bigquery.SchemaField('person_ctry_code', STR, NULL, None, ()),
            bigquery.SchemaField('residence_ctry_code', STR, NULL, None, ()),
            bigquery.SchemaField('role', STR, NULL, None, ())
        ]
        
        self.tls227 = [
            bigquery.SchemaField('person_id', INT, REQ, None, ()),
            bigquery.SchemaField('pat_publn_id', INT, NULL, None, ()),
            bigquery.SchemaField('applt_seq_nr', INT, NULL, None, ()),
            bigquery.SchemaField('invt_seq_nr', INT, NULL, None, ())
        ]
        
        self.tls229 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('nace2_code', STR, NULL, None, ()),
            bigquery.SchemaField('weight', FLO, NULL, None, ())
        ]
        
        self.tls230 = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('techn_field_nr', INT, NULL, None, ()),
            bigquery.SchemaField('weight', FLO, NULL, None, ())
        ]
        
        self.tls231 = [
            bigquery.SchemaField('event_id', INT, REQ, None, ()),
            bigquery.SchemaField('appln_id', INT, NULL, None, ()),
            bigquery.SchemaField('event_seq_nr', INT, NULL, None, ()),
            bigquery.SchemaField('event_type', STR, NULL, None, ()),
            bigquery.SchemaField('event_auth', STR, NULL, None, ()),
            bigquery.SchemaField('event_code', STR, NULL, None, ()),
            bigquery.SchemaField('event_filing_date', DAT, NULL, None, ()),
            bigquery.SchemaField('event_publn_date', DAT, NULL, None, ()),
            bigquery.SchemaField('event_effective_date', DAT, NULL, None, ()),
            bigquery.SchemaField('event_text', STR, NULL, None, ()),
            bigquery.SchemaField('ref_doc_auth', STR, NULL, None, ()),
            bigquery.SchemaField('ref_doc_nr', STR, NULL, None, ()),
            bigquery.SchemaField('ref_doc_kind', STR, NULL, None, ()),
            bigquery.SchemaField('ref_doc_date', DAT, NULL, None, ()),
            bigquery.SchemaField('ref_doc_text', STR, NULL, None, ()),
            bigquery.SchemaField('party_type', STR, NULL, None, ()),
            bigquery.SchemaField('party_seq_nr', INT, NULL, None, ()),
            bigquery.SchemaField('party_new', STR, NULL, None, ()),
            bigquery.SchemaField('party_old', STR, NULL, None, ()),
            bigquery.SchemaField('spc_nr', STR, NULL, None, ()),
            bigquery.SchemaField('spc_filing_date', DAT, NULL, None, ()),
            bigquery.SchemaField('spc_patent_expiry_date', DAT, NULL, None, ()),
            bigquery.SchemaField('spc_extension_date', DAT, NULL, None, ()),
            bigquery.SchemaField('spc_text', STR, NULL, None, ()),
            bigquery.SchemaField('designated_states', STR, NULL, None, ()),
            bigquery.SchemaField('extension_states', STR, NULL, None, ()),
            bigquery.SchemaField('fee_country', STR, NULL, None, ()),
            bigquery.SchemaField('fee_payment_date', DAT, NULL, None, ()),
            bigquery.SchemaField('fee_renewal_year', INT, NULL, None, ()),
            bigquery.SchemaField('fee_text', STR, NULL, None, ()),
            bigquery.SchemaField('lapse_country', STR, NULL, None, ()),
            bigquery.SchemaField('lapse_date', DAT, NULL, None, ()),
            bigquery.SchemaField('lapse_text', STR, NULL, None, ()),
            bigquery.SchemaField('reinstate_country', STR, NULL, None, ()),
            bigquery.SchemaField('reinstate_date', DAT, NULL, None, ()),
            bigquery.SchemaField('reinstate_text', STR, NULL, None, ()),
            bigquery.SchemaField('class_scheme', STR, NULL, None, ()),
            bigquery.SchemaField('class_symbol', STR, NULL, None, ())
        ]
        
        self.tls801 = [
            bigquery.SchemaField('ctry_code', STR, REQ, None, ()),
            bigquery.SchemaField('iso_alpha3', STR, NULL, None, ()),
            bigquery.SchemaField('st3_name', STR, NULL, None, ()),
            bigquery.SchemaField('state_indicator', STR, NULL, None, ()),
            bigquery.SchemaField('continent', STR, NULL, None, ()),
            bigquery.SchemaField('eu_member', STR, NULL, None, ()),
            bigquery.SchemaField('epo_member', STR, NULL, None, ()),
            bigquery.SchemaField('oecd_member', STR, NULL, None, ()),
            bigquery.SchemaField('discontinued', STR, NULL, None, ())
        ]
        
        self.tls803 = [
            bigquery.SchemaField('event_auth', STR, REQ, None, ()),
            bigquery.SchemaField('event_code', STR, NULL, None, ()),
            bigquery.SchemaField('event_impact', STR, NULL, None, ()),
            bigquery.SchemaField('event_descr', STR, NULL, None, ()),
            bigquery.SchemaField('event_descr_orig', STR, NULL, None, ()),
            bigquery.SchemaField('event_category_code', STR, NULL, None, ()),
            bigquery.SchemaField('event_category_title', STR, NULL, None, ())
        ]
        
        self.tls901 = [
            bigquery.SchemaField('ipc_maingroup_symbol', STR, REQ, None, ()),
            bigquery.SchemaField('techn_field_nr', INT, NULL, None, ()),
            bigquery.SchemaField('techn_sector', STR, NULL, None, ()),
            bigquery.SchemaField('techn_field', STR, NULL, None, ())
        ]
        
        self.tls902 = [
            bigquery.SchemaField('ipc', STR, REQ, None, ()),
            bigquery.SchemaField('not_with_ipc', STR, NULL, None, ()),
            bigquery.SchemaField('unless_with_ipc', STR, NULL, None, ()),
            bigquery.SchemaField('nace2_code', STR, NULL, None, ()),
            bigquery.SchemaField('nace2_weight', STR, NULL, None, ()),
            bigquery.SchemaField('nace2_descr', STR, NULL, None, ())
        ]
        
        self.tls904 = [
            bigquery.SchemaField('nuts', STR, REQ, None, ()),
            bigquery.SchemaField('nuts_level', INT, NULL, None, ()),
            bigquery.SchemaField('nuts_label', STR, NULL, None, ())
        ]
        
        self.tls906 = [
            bigquery.SchemaField('person_id', INT, REQ, None, ()),
            bigquery.SchemaField('person_name', STR, NULL, None, ()),
            bigquery.SchemaField('person_address', STR, NULL, None, ()),
            bigquery.SchemaField('person_ctry_code', STR, NULL, None, ()),
            bigquery.SchemaField('nuts', STR, NULL, None, ()),
            bigquery.SchemaField('nuts_level', INT, NULL, None, ()),
            bigquery.SchemaField('doc_std_name_id', INT, NULL, None, ()),
            bigquery.SchemaField('doc_std_name', STR, NULL, None, ()),
            bigquery.SchemaField('psn_id', INT, NULL, None, ()),
            bigquery.SchemaField('psn_name', STR, NULL, None, ()),
            bigquery.SchemaField('psn_level', INT, NULL, None, ()),
            bigquery.SchemaField('psn_sector', STR, NULL, None, ()),
            bigquery.SchemaField('han_id', INT, NULL, None, ()),
            bigquery.SchemaField('han_name', STR, NULL, None, ()),
            bigquery.SchemaField('han_harmonized', INT, NULL, None, ())
        ]

        self.tls2012_wordcount = [
            bigquery.SchemaField('appln_title_lg', STR, NULL, None, ()),
            bigquery.SchemaField('appln_auth', STR, NULL, None, ()),
            bigquery.SchemaField('year', INT, NULL, None, (), ),
            bigquery.SchemaField('word', STR, NULL, None, ()),
            bigquery.SchemaField('count', INT, NULL, None, ()),
        ]
        self.inv_geo = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('patent_office', STR, NULL, None, ()),
            bigquery.SchemaField('priority_date', DAT, NULL, None, ()),
            bigquery.SchemaField('name_0', STR, NULL, None, ()),
            bigquery.SchemaField('name_1', STR, NULL, None, ()),
            bigquery.SchemaField('name_2', STR, NULL, None, ()),
            bigquery.SchemaField('name_3', STR, NULL, None, ()),
            bigquery.SchemaField('name_4', STR, NULL, None, ()),
            bigquery.SchemaField('name_5', STR, NULL, None, ()),
            bigquery.SchemaField('city', STR, NULL, None, ()),
            bigquery.SchemaField('lat', FLO, NULL, None, ()),
            bigquery.SchemaField('lng', FLO, NULL, None, ()),
            bigquery.SchemaField('data_source', STR, NULL, None, ()),
            bigquery.SchemaField('coord_source', STR, NULL, None, ()),
            bigquery.SchemaField('source', INT, NULL, None, ()),
            bigquery.SchemaField('priority_year', INT, NULL, None, ())
        ]
        self.app_geo = [
            bigquery.SchemaField('appln_id', INT, REQ, None, ()),
            bigquery.SchemaField('patent_office', STR, NULL, None, ()),
            bigquery.SchemaField('priority_date', DAT, NULL, None, ()),
            bigquery.SchemaField('name_0', STR, NULL, None, ()),
            bigquery.SchemaField('name_1', STR, NULL, None, ()),
            bigquery.SchemaField('name_2', STR, NULL, None, ()),
            bigquery.SchemaField('name_3', STR, NULL, None, ()),
            bigquery.SchemaField('name_4', STR, NULL, None, ()),
            bigquery.SchemaField('name_5', STR, NULL, None, ()),
            bigquery.SchemaField('city', STR, NULL, None, ()),
            bigquery.SchemaField('lat', FLO, NULL, None, ()),
            bigquery.SchemaField('lng', FLO, NULL, None, ()),
            bigquery.SchemaField('data_source', STR, NULL, None, ()),
            bigquery.SchemaField('coord_source', STR, NULL, None, ()),
            bigquery.SchemaField('source', INT, NULL, None, ()),
            bigquery.SchemaField('priority_year', INT, NULL, None, ())
        ]
        self.date_utils = [
            bigquery.SchemaField('date', DAT, NULL, None, ()),
            bigquery.SchemaField('year', INT, NULL, None, ())
        ]
        
        self.rawexaminer = [ 					
            bigquery.SchemaField('uuid', STR, REQ, None, ()),
            bigquery.SchemaField('patent_id', STR, NULL, None, ()),
            bigquery.SchemaField('name_first', STR, NULL, None, ()),
            bigquery.SchemaField('name_last', STR, NULL, None, ()),
            bigquery.SchemaField('role', STR, NULL, None, ()),
            bigquery.SchemaField('group', STR, NULL, None, ())
        ]
        
        self.rawlawyer = [ 
            bigquery.SchemaField('uuid', STR, REQ, None, ()),
            bigquery.SchemaField('lawyer_id', STR, NULL, None, ()),
            bigquery.SchemaField('patent_id', STR, NULL, None, ()),
            bigquery.SchemaField('name_first', STR, NULL, None, ()),
            bigquery.SchemaField('name_last', STR, NULL, None, ()),
            bigquery.SchemaField('organization', STR, NULL, None, ()),
            bigquery.SchemaField('country', STR, NULL, None, ()),
            bigquery.SchemaField('sequence', INT, NULL, None, ())
        ]
        
        self.application = [ 					
            bigquery.SchemaField('id', STR, REQ, None, ()),
            bigquery.SchemaField('patent_id', STR, REQ, None, ()),
            bigquery.SchemaField('series_code', INT, NULL, None, ()),
            bigquery.SchemaField('number', INT, NULL, None, ()),
            bigquery.SchemaField('country', STR, NULL, None, ()),
            bigquery.SchemaField('date', DAT, NULL, None, ())
        ]
        
        self.patent = [ 
            bigquery.SchemaField('id', INT, REQ, None, ()),
            bigquery.SchemaField('type', STR, REQ, None, ()),
            bigquery.SchemaField('number', INT, NULL, None, ()),
            bigquery.SchemaField('country', STR, NULL, None, ()),
            bigquery.SchemaField('date', DAT, NULL, None, ()),
            bigquery.SchemaField('abstract', STR, NULL, None, ()),
            bigquery.SchemaField('title', STR, NULL, None, ()),
            bigquery.SchemaField('kind', STR, NULL, None, ()),
            bigquery.SchemaField('num_claims', INT, NULL, None, ()),
            bigquery.SchemaField('filename', STR, NULL, None, ()),
            bigquery.SchemaField('withdrawn', STR, NULL, None, ())
        ]
        
        self.mapping = [
            bigquery.SchemaField('patent_id', STR, REQ, None, ()),
            bigquery.SchemaField('appln_id', INT, REQ, None, ())
        ]
