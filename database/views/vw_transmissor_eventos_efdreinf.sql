-- eMensageriaAI --
-- View: public.vw_transmissor_eventos_efdreinf

DROP VIEW IF EXISTS public.vw_transmissor_eventos_efdreinf;

CREATE OR REPLACE VIEW public.vw_transmissor_eventos_efdreinf AS SELECT r1000_evtinfocontri.id,
    'r1000'::text AS evento,
    r1000_evtinfocontri.identidade,
    r1000_evtinfocontri.transmissor_lote_efdreinf_id,
    r1000_evtinfocontri.criado_em,
    r1000_evtinfocontri.criado_por_id,
    r1000_evtinfocontri.modificado_em,
    r1000_evtinfocontri.modificado_por_id,
    r1000_evtinfocontri.desativado_em,
    r1000_evtinfocontri.desativado_por_id,
    r1000_evtinfocontri.ativo,
    1 AS grupo,
    'r1000_evtinfocontri'::text AS tabela,
    'r1000_evtinfocontri_salvar'::text AS tabela_salvar,
    r1000_evtinfocontri.id AS ordem,
    r1000_evtinfocontri.tpinsc,
    r1000_evtinfocontri.nrinsc,
    'r1000_evtinfocontri_recibo'::text AS url_recibo,
    r1000_evtinfocontri.validacao_precedencia,
    r1000_evtinfocontri.validacoes,
    r1000_evtinfocontri.status,
    r1000_evtinfocontri.retorno_envio_json,
    r1000_evtinfocontri.retorno_consulta_json,
    r1000_evtinfocontri.evento_json,
    r1000_evtinfocontri.ocorrencias_json,
    r1000_evtinfocontri.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r1000_evtinfocontri
   LEFT JOIN transmissor_lote_efdreinf lt ON r1000_evtinfocontri.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r1000_evtinfocontri.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r1000_evtinfocontri.ativo = true
 UNION
SELECT r1070_evttabprocesso.id,
    'r1070'::text AS evento,
    r1070_evttabprocesso.identidade,
    r1070_evttabprocesso.transmissor_lote_efdreinf_id,
    r1070_evttabprocesso.criado_em,
    r1070_evttabprocesso.criado_por_id,
    r1070_evttabprocesso.modificado_em,
    r1070_evttabprocesso.modificado_por_id,
    r1070_evttabprocesso.desativado_em,
    r1070_evttabprocesso.desativado_por_id,
    r1070_evttabprocesso.ativo,
    1 AS grupo,
    'r1070_evttabprocesso'::text AS tabela,
    'r1070_evttabprocesso_salvar'::text AS tabela_salvar,
    r1070_evttabprocesso.id AS ordem,
    r1070_evttabprocesso.tpinsc,
    r1070_evttabprocesso.nrinsc,
    'r1070_evttabprocesso_recibo'::text AS url_recibo,
    r1070_evttabprocesso.validacao_precedencia,
    r1070_evttabprocesso.validacoes,
    r1070_evttabprocesso.status,
    r1070_evttabprocesso.retorno_envio_json,
    r1070_evttabprocesso.retorno_consulta_json,
    r1070_evttabprocesso.evento_json,
    r1070_evttabprocesso.ocorrencias_json,
    r1070_evttabprocesso.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r1070_evttabprocesso
   LEFT JOIN transmissor_lote_efdreinf lt ON r1070_evttabprocesso.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r1070_evttabprocesso.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r1070_evttabprocesso.ativo = true
 UNION
SELECT r2010_evtservtom.id,
    'r2010'::text AS evento,
    r2010_evtservtom.identidade,
    r2010_evtservtom.transmissor_lote_efdreinf_id,
    r2010_evtservtom.criado_em,
    r2010_evtservtom.criado_por_id,
    r2010_evtservtom.modificado_em,
    r2010_evtservtom.modificado_por_id,
    r2010_evtservtom.desativado_em,
    r2010_evtservtom.desativado_por_id,
    r2010_evtservtom.ativo,
    3 AS grupo,
    'r2010_evtservtom'::text AS tabela,
    'r2010_evtservtom_salvar'::text AS tabela_salvar,
    r2010_evtservtom.id AS ordem,
    r2010_evtservtom.tpinsc,
    r2010_evtservtom.nrinsc,
    'r2010_evtservtom_recibo'::text AS url_recibo,
    r2010_evtservtom.validacao_precedencia,
    r2010_evtservtom.validacoes,
    r2010_evtservtom.status,
    r2010_evtservtom.retorno_envio_json,
    r2010_evtservtom.retorno_consulta_json,
    r2010_evtservtom.evento_json,
    r2010_evtservtom.ocorrencias_json,
    r2010_evtservtom.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2010_evtservtom
   LEFT JOIN transmissor_lote_efdreinf lt ON r2010_evtservtom.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2010_evtservtom.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2010_evtservtom.ativo = true
 UNION
SELECT r2020_evtservprest.id,
    'r2020'::text AS evento,
    r2020_evtservprest.identidade,
    r2020_evtservprest.transmissor_lote_efdreinf_id,
    r2020_evtservprest.criado_em,
    r2020_evtservprest.criado_por_id,
    r2020_evtservprest.modificado_em,
    r2020_evtservprest.modificado_por_id,
    r2020_evtservprest.desativado_em,
    r2020_evtservprest.desativado_por_id,
    r2020_evtservprest.ativo,
    3 AS grupo,
    'r2020_evtservprest'::text AS tabela,
    'r2020_evtservprest_salvar'::text AS tabela_salvar,
    r2020_evtservprest.id AS ordem,
    r2020_evtservprest.tpinsc,
    r2020_evtservprest.nrinsc,
    'r2020_evtservprest_recibo'::text AS url_recibo,
    r2020_evtservprest.validacao_precedencia,
    r2020_evtservprest.validacoes,
    r2020_evtservprest.status,
    r2020_evtservprest.retorno_envio_json,
    r2020_evtservprest.retorno_consulta_json,
    r2020_evtservprest.evento_json,
    r2020_evtservprest.ocorrencias_json,
    r2020_evtservprest.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2020_evtservprest
   LEFT JOIN transmissor_lote_efdreinf lt ON r2020_evtservprest.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2020_evtservprest.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2020_evtservprest.ativo = true
 UNION
SELECT r2030_evtassocdesprec.id,
    'r2030'::text AS evento,
    r2030_evtassocdesprec.identidade,
    r2030_evtassocdesprec.transmissor_lote_efdreinf_id,
    r2030_evtassocdesprec.criado_em,
    r2030_evtassocdesprec.criado_por_id,
    r2030_evtassocdesprec.modificado_em,
    r2030_evtassocdesprec.modificado_por_id,
    r2030_evtassocdesprec.desativado_em,
    r2030_evtassocdesprec.desativado_por_id,
    r2030_evtassocdesprec.ativo,
    3 AS grupo,
    'r2030_evtassocdesprec'::text AS tabela,
    'r2030_evtassocdesprec_salvar'::text AS tabela_salvar,
    r2030_evtassocdesprec.id AS ordem,
    r2030_evtassocdesprec.tpinsc,
    r2030_evtassocdesprec.nrinsc,
    'r2030_evtassocdesprec_recibo'::text AS url_recibo,
    r2030_evtassocdesprec.validacao_precedencia,
    r2030_evtassocdesprec.validacoes,
    r2030_evtassocdesprec.status,
    r2030_evtassocdesprec.retorno_envio_json,
    r2030_evtassocdesprec.retorno_consulta_json,
    r2030_evtassocdesprec.evento_json,
    r2030_evtassocdesprec.ocorrencias_json,
    r2030_evtassocdesprec.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2030_evtassocdesprec
   LEFT JOIN transmissor_lote_efdreinf lt ON r2030_evtassocdesprec.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2030_evtassocdesprec.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2030_evtassocdesprec.ativo = true
 UNION
SELECT r2040_evtassocdesprep.id,
    'r2040'::text AS evento,
    r2040_evtassocdesprep.identidade,
    r2040_evtassocdesprep.transmissor_lote_efdreinf_id,
    r2040_evtassocdesprep.criado_em,
    r2040_evtassocdesprep.criado_por_id,
    r2040_evtassocdesprep.modificado_em,
    r2040_evtassocdesprep.modificado_por_id,
    r2040_evtassocdesprep.desativado_em,
    r2040_evtassocdesprep.desativado_por_id,
    r2040_evtassocdesprep.ativo,
    3 AS grupo,
    'r2040_evtassocdesprep'::text AS tabela,
    'r2040_evtassocdesprep_salvar'::text AS tabela_salvar,
    r2040_evtassocdesprep.id AS ordem,
    r2040_evtassocdesprep.tpinsc,
    r2040_evtassocdesprep.nrinsc,
    'r2040_evtassocdesprep_recibo'::text AS url_recibo,
    r2040_evtassocdesprep.validacao_precedencia,
    r2040_evtassocdesprep.validacoes,
    r2040_evtassocdesprep.status,
    r2040_evtassocdesprep.retorno_envio_json,
    r2040_evtassocdesprep.retorno_consulta_json,
    r2040_evtassocdesprep.evento_json,
    r2040_evtassocdesprep.ocorrencias_json,
    r2040_evtassocdesprep.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2040_evtassocdesprep
   LEFT JOIN transmissor_lote_efdreinf lt ON r2040_evtassocdesprep.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2040_evtassocdesprep.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2040_evtassocdesprep.ativo = true
 UNION
SELECT r2050_evtcomprod.id,
    'r2050'::text AS evento,
    r2050_evtcomprod.identidade,
    r2050_evtcomprod.transmissor_lote_efdreinf_id,
    r2050_evtcomprod.criado_em,
    r2050_evtcomprod.criado_por_id,
    r2050_evtcomprod.modificado_em,
    r2050_evtcomprod.modificado_por_id,
    r2050_evtcomprod.desativado_em,
    r2050_evtcomprod.desativado_por_id,
    r2050_evtcomprod.ativo,
    3 AS grupo,
    'r2050_evtcomprod'::text AS tabela,
    'r2050_evtcomprod_salvar'::text AS tabela_salvar,
    r2050_evtcomprod.id AS ordem,
    r2050_evtcomprod.tpinsc,
    r2050_evtcomprod.nrinsc,
    'r2050_evtcomprod_recibo'::text AS url_recibo,
    r2050_evtcomprod.validacao_precedencia,
    r2050_evtcomprod.validacoes,
    r2050_evtcomprod.status,
    r2050_evtcomprod.retorno_envio_json,
    r2050_evtcomprod.retorno_consulta_json,
    r2050_evtcomprod.evento_json,
    r2050_evtcomprod.ocorrencias_json,
    r2050_evtcomprod.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2050_evtcomprod
   LEFT JOIN transmissor_lote_efdreinf lt ON r2050_evtcomprod.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2050_evtcomprod.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2050_evtcomprod.ativo = true
 UNION
SELECT r2060_evtcprb.id,
    'r2060'::text AS evento,
    r2060_evtcprb.identidade,
    r2060_evtcprb.transmissor_lote_efdreinf_id,
    r2060_evtcprb.criado_em,
    r2060_evtcprb.criado_por_id,
    r2060_evtcprb.modificado_em,
    r2060_evtcprb.modificado_por_id,
    r2060_evtcprb.desativado_em,
    r2060_evtcprb.desativado_por_id,
    r2060_evtcprb.ativo,
    3 AS grupo,
    'r2060_evtcprb'::text AS tabela,
    'r2060_evtcprb_salvar'::text AS tabela_salvar,
    r2060_evtcprb.id AS ordem,
    r2060_evtcprb.tpinsc,
    r2060_evtcprb.nrinsc,
    'r2060_evtcprb_recibo'::text AS url_recibo,
    r2060_evtcprb.validacao_precedencia,
    r2060_evtcprb.validacoes,
    r2060_evtcprb.status,
    r2060_evtcprb.retorno_envio_json,
    r2060_evtcprb.retorno_consulta_json,
    r2060_evtcprb.evento_json,
    r2060_evtcprb.ocorrencias_json,
    r2060_evtcprb.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2060_evtcprb
   LEFT JOIN transmissor_lote_efdreinf lt ON r2060_evtcprb.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2060_evtcprb.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2060_evtcprb.ativo = true
 UNION
SELECT r2070_evtpgtosdivs.id,
    'r2070'::text AS evento,
    r2070_evtpgtosdivs.identidade,
    r2070_evtpgtosdivs.transmissor_lote_efdreinf_id,
    r2070_evtpgtosdivs.criado_em,
    r2070_evtpgtosdivs.criado_por_id,
    r2070_evtpgtosdivs.modificado_em,
    r2070_evtpgtosdivs.modificado_por_id,
    r2070_evtpgtosdivs.desativado_em,
    r2070_evtpgtosdivs.desativado_por_id,
    r2070_evtpgtosdivs.ativo,
    3 AS grupo,
    'r2070_evtpgtosdivs'::text AS tabela,
    'r2070_evtpgtosdivs_salvar'::text AS tabela_salvar,
    r2070_evtpgtosdivs.id AS ordem,
    r2070_evtpgtosdivs.tpinsc,
    r2070_evtpgtosdivs.nrinsc,
    'r2070_evtpgtosdivs_recibo'::text AS url_recibo,
    r2070_evtpgtosdivs.validacao_precedencia,
    r2070_evtpgtosdivs.validacoes,
    r2070_evtpgtosdivs.status,
    r2070_evtpgtosdivs.retorno_envio_json,
    r2070_evtpgtosdivs.retorno_consulta_json,
    r2070_evtpgtosdivs.evento_json,
    r2070_evtpgtosdivs.ocorrencias_json,
    r2070_evtpgtosdivs.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2070_evtpgtosdivs
   LEFT JOIN transmissor_lote_efdreinf lt ON r2070_evtpgtosdivs.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2070_evtpgtosdivs.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2070_evtpgtosdivs.ativo = true
 UNION
SELECT r2098_evtreabreevper.id,
    'r2098'::text AS evento,
    r2098_evtreabreevper.identidade,
    r2098_evtreabreevper.transmissor_lote_efdreinf_id,
    r2098_evtreabreevper.criado_em,
    r2098_evtreabreevper.criado_por_id,
    r2098_evtreabreevper.modificado_em,
    r2098_evtreabreevper.modificado_por_id,
    r2098_evtreabreevper.desativado_em,
    r2098_evtreabreevper.desativado_por_id,
    r2098_evtreabreevper.ativo,
    3 AS grupo,
    'r2098_evtreabreevper'::text AS tabela,
    'r2098_evtreabreevper_salvar'::text AS tabela_salvar,
    r2098_evtreabreevper.id AS ordem,
    r2098_evtreabreevper.tpinsc,
    r2098_evtreabreevper.nrinsc,
    'r2098_evtreabreevper_recibo'::text AS url_recibo,
    r2098_evtreabreevper.validacao_precedencia,
    r2098_evtreabreevper.validacoes,
    r2098_evtreabreevper.status,
    r2098_evtreabreevper.retorno_envio_json,
    r2098_evtreabreevper.retorno_consulta_json,
    r2098_evtreabreevper.evento_json,
    r2098_evtreabreevper.ocorrencias_json,
    r2098_evtreabreevper.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2098_evtreabreevper
   LEFT JOIN transmissor_lote_efdreinf lt ON r2098_evtreabreevper.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2098_evtreabreevper.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2098_evtreabreevper.ativo = true
 UNION
SELECT r2099_evtfechaevper.id,
    'r2099'::text AS evento,
    r2099_evtfechaevper.identidade,
    r2099_evtfechaevper.transmissor_lote_efdreinf_id,
    r2099_evtfechaevper.criado_em,
    r2099_evtfechaevper.criado_por_id,
    r2099_evtfechaevper.modificado_em,
    r2099_evtfechaevper.modificado_por_id,
    r2099_evtfechaevper.desativado_em,
    r2099_evtfechaevper.desativado_por_id,
    r2099_evtfechaevper.ativo,
    3 AS grupo,
    'r2099_evtfechaevper'::text AS tabela,
    'r2099_evtfechaevper_salvar'::text AS tabela_salvar,
    r2099_evtfechaevper.id AS ordem,
    r2099_evtfechaevper.tpinsc,
    r2099_evtfechaevper.nrinsc,
    'r2099_evtfechaevper_recibo'::text AS url_recibo,
    r2099_evtfechaevper.validacao_precedencia,
    r2099_evtfechaevper.validacoes,
    r2099_evtfechaevper.status,
    r2099_evtfechaevper.retorno_envio_json,
    r2099_evtfechaevper.retorno_consulta_json,
    r2099_evtfechaevper.evento_json,
    r2099_evtfechaevper.ocorrencias_json,
    r2099_evtfechaevper.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r2099_evtfechaevper
   LEFT JOIN transmissor_lote_efdreinf lt ON r2099_evtfechaevper.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r2099_evtfechaevper.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r2099_evtfechaevper.ativo = true
 UNION
SELECT r3010_evtespdesportivo.id,
    'r3010'::text AS evento,
    r3010_evtespdesportivo.identidade,
    r3010_evtespdesportivo.transmissor_lote_efdreinf_id,
    r3010_evtespdesportivo.criado_em,
    r3010_evtespdesportivo.criado_por_id,
    r3010_evtespdesportivo.modificado_em,
    r3010_evtespdesportivo.modificado_por_id,
    r3010_evtespdesportivo.desativado_em,
    r3010_evtespdesportivo.desativado_por_id,
    r3010_evtespdesportivo.ativo,
    3 AS grupo,
    'r3010_evtespdesportivo'::text AS tabela,
    'r3010_evtespdesportivo_salvar'::text AS tabela_salvar,
    r3010_evtespdesportivo.id AS ordem,
    r3010_evtespdesportivo.tpinsc,
    r3010_evtespdesportivo.nrinsc,
    'r3010_evtespdesportivo_recibo'::text AS url_recibo,
    r3010_evtespdesportivo.validacao_precedencia,
    r3010_evtespdesportivo.validacoes,
    r3010_evtespdesportivo.status,
    r3010_evtespdesportivo.retorno_envio_json,
    r3010_evtespdesportivo.retorno_consulta_json,
    r3010_evtespdesportivo.evento_json,
    r3010_evtespdesportivo.ocorrencias_json,
    r3010_evtespdesportivo.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r3010_evtespdesportivo
   LEFT JOIN transmissor_lote_efdreinf lt ON r3010_evtespdesportivo.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r3010_evtespdesportivo.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r3010_evtespdesportivo.ativo = true
 UNION
SELECT r9000_evtexclusao.id,
    'r9000'::text AS evento,
    r9000_evtexclusao.identidade,
    r9000_evtexclusao.transmissor_lote_efdreinf_id,
    r9000_evtexclusao.criado_em,
    r9000_evtexclusao.criado_por_id,
    r9000_evtexclusao.modificado_em,
    r9000_evtexclusao.modificado_por_id,
    r9000_evtexclusao.desativado_em,
    r9000_evtexclusao.desativado_por_id,
    r9000_evtexclusao.ativo,
    2 AS grupo,
    'r9000_evtexclusao'::text AS tabela,
    'r9000_evtexclusao_salvar'::text AS tabela_salvar,
    r9000_evtexclusao.id AS ordem,
    r9000_evtexclusao.tpinsc,
    r9000_evtexclusao.nrinsc,
    'r9000_evtexclusao_recibo'::text AS url_recibo,
    r9000_evtexclusao.validacao_precedencia,
    r9000_evtexclusao.validacoes,
    r9000_evtexclusao.status,
    r9000_evtexclusao.retorno_envio_json,
    r9000_evtexclusao.retorno_consulta_json,
    r9000_evtexclusao.evento_json,
    r9000_evtexclusao.ocorrencias_json,
    r9000_evtexclusao.transmissor_lote_efdreinf_error_id,
    COALESCE(lt.data_hora_envio, lte.data_hora_envio) AS data_hora_envio,
    COALESCE(lt.data_hora_consulta, lte.data_hora_consulta) AS data_hora_consulta
   FROM r9000_evtexclusao
   LEFT JOIN transmissor_lote_efdreinf lt ON r9000_evtexclusao.transmissor_lote_efdreinf_id = lt.id
   LEFT JOIN transmissor_lote_efdreinf lte ON r9000_evtexclusao.transmissor_lote_efdreinf_error_id = lte.id
  WHERE r9000_evtexclusao.ativo = true;