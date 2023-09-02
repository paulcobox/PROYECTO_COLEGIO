--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ALUMNO; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."ALUMNO" (
    "NOMBRE" character varying(100) NOT NULL,
    "EDAD" integer NOT NULL,
    "ID_ALUMNO" integer NOT NULL,
    "CORRE0" character varying(100) NOT NULL
);


ALTER TABLE public."ALUMNO" OWNER TO postgres;

--
-- Name: ALUMNO_ID_ALUMNO_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."ALUMNO_ID_ALUMNO_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."ALUMNO_ID_ALUMNO_seq" OWNER TO postgres;

--
-- Name: ALUMNO_ID_ALUMNO_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."ALUMNO_ID_ALUMNO_seq" OWNED BY public."ALUMNO"."ID_ALUMNO";


--
-- Name: CURSO; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."CURSO" (
    "ID_CURSO" integer NOT NULL,
    "NOMBRE" character varying(100) NOT NULL
);


ALTER TABLE public."CURSO" OWNER TO postgres;

--
-- Name: CURSO_ID_CURSO_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."CURSO_ID_CURSO_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."CURSO_ID_CURSO_seq" OWNER TO postgres;

--
-- Name: CURSO_ID_CURSO_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."CURSO_ID_CURSO_seq" OWNED BY public."CURSO"."ID_CURSO";


--
-- Name: MALLA_CURRICULAR; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MALLA_CURRICULAR" (
    "ID_PROFESOR_CURSO" integer NOT NULL,
    "ID_PERIODO" integer NOT NULL,
    "ID_SALON" integer NOT NULL,
    "ID_MALLA_CURRICULAR" integer NOT NULL
);


ALTER TABLE public."MALLA_CURRICULAR" OWNER TO postgres;

--
-- Name: MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq" OWNER TO postgres;

--
-- Name: MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq" OWNED BY public."MALLA_CURRICULAR"."ID_MALLA_CURRICULAR";


--
-- Name: NOTA; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."NOTA" (
    "ID_MALLA_CURRICULAR" integer,
    "NOTA" integer,
    "ID_ALUMNO" integer,
    "ID_NOTA" integer NOT NULL
);


ALTER TABLE public."NOTA" OWNER TO postgres;

--
-- Name: NOTA_ID_NOTA_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."NOTA_ID_NOTA_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."NOTA_ID_NOTA_seq" OWNER TO postgres;

--
-- Name: NOTA_ID_NOTA_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."NOTA_ID_NOTA_seq" OWNED BY public."NOTA"."ID_NOTA";


--
-- Name: PERIODO_ESCOLAR; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PERIODO_ESCOLAR" (
    "AÑO" integer NOT NULL,
    "CICLO" integer NOT NULL,
    "FECHA_DESDE" date NOT NULL,
    "FECHA_HASTA" date NOT NULL,
    "ID_PERIODO" integer NOT NULL
);


ALTER TABLE public."PERIODO_ESCOLAR" OWNER TO postgres;

--
-- Name: PERIODO_ESCOLAR_ID_PERIODO_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."PERIODO_ESCOLAR_ID_PERIODO_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."PERIODO_ESCOLAR_ID_PERIODO_seq" OWNER TO postgres;

--
-- Name: PERIODO_ESCOLAR_ID_PERIODO_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."PERIODO_ESCOLAR_ID_PERIODO_seq" OWNED BY public."PERIODO_ESCOLAR"."ID_PERIODO";


--
-- Name: PROFESOR; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PROFESOR" (
    "ID_PROFESOR" integer NOT NULL,
    "NOMBRE" character varying(100) NOT NULL,
    "EDAD" integer NOT NULL,
    "CORREO" character varying(100) NOT NULL
);


ALTER TABLE public."PROFESOR" OWNER TO postgres;

--
-- Name: PROFESOR_CURSO; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PROFESOR_CURSO" (
    "ID_CURSO" integer NOT NULL,
    "ID_PROFESOR" integer NOT NULL,
    "ID_PROFESOR_CURSO" integer NOT NULL
);


ALTER TABLE public."PROFESOR_CURSO" OWNER TO postgres;

--
-- Name: PROFESOR_CURSO_ID_PROFESOR_CURSO_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."PROFESOR_CURSO_ID_PROFESOR_CURSO_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."PROFESOR_CURSO_ID_PROFESOR_CURSO_seq" OWNER TO postgres;

--
-- Name: PROFESOR_CURSO_ID_PROFESOR_CURSO_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."PROFESOR_CURSO_ID_PROFESOR_CURSO_seq" OWNED BY public."PROFESOR_CURSO"."ID_PROFESOR_CURSO";


--
-- Name: PROFESOR_ID_PROFESOR_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."PROFESOR_ID_PROFESOR_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."PROFESOR_ID_PROFESOR_seq" OWNER TO postgres;

--
-- Name: PROFESOR_ID_PROFESOR_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."PROFESOR_ID_PROFESOR_seq" OWNED BY public."PROFESOR"."ID_PROFESOR";


--
-- Name: SALON; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SALON" (
    "ID_SALON" integer NOT NULL,
    "NOMBRE" character varying(50) NOT NULL
);


ALTER TABLE public."SALON" OWNER TO postgres;

--
-- Name: SALON_ID_SALON_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."SALON_ID_SALON_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."SALON_ID_SALON_seq" OWNER TO postgres;

--
-- Name: SALON_ID_SALON_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."SALON_ID_SALON_seq" OWNED BY public."SALON"."ID_SALON";


--
-- Name: ALUMNO ID_ALUMNO; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ALUMNO" ALTER COLUMN "ID_ALUMNO" SET DEFAULT nextval('public."ALUMNO_ID_ALUMNO_seq"'::regclass);


--
-- Name: CURSO ID_CURSO; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."CURSO" ALTER COLUMN "ID_CURSO" SET DEFAULT nextval('public."CURSO_ID_CURSO_seq"'::regclass);


--
-- Name: MALLA_CURRICULAR ID_MALLA_CURRICULAR; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MALLA_CURRICULAR" ALTER COLUMN "ID_MALLA_CURRICULAR" SET DEFAULT nextval('public."MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq"'::regclass);


--
-- Name: NOTA ID_NOTA; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NOTA" ALTER COLUMN "ID_NOTA" SET DEFAULT nextval('public."NOTA_ID_NOTA_seq"'::regclass);


--
-- Name: PERIODO_ESCOLAR ID_PERIODO; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PERIODO_ESCOLAR" ALTER COLUMN "ID_PERIODO" SET DEFAULT nextval('public."PERIODO_ESCOLAR_ID_PERIODO_seq"'::regclass);


--
-- Name: PROFESOR ID_PROFESOR; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PROFESOR" ALTER COLUMN "ID_PROFESOR" SET DEFAULT nextval('public."PROFESOR_ID_PROFESOR_seq"'::regclass);


--
-- Name: PROFESOR_CURSO ID_PROFESOR_CURSO; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PROFESOR_CURSO" ALTER COLUMN "ID_PROFESOR_CURSO" SET DEFAULT nextval('public."PROFESOR_CURSO_ID_PROFESOR_CURSO_seq"'::regclass);


--
-- Name: SALON ID_SALON; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SALON" ALTER COLUMN "ID_SALON" SET DEFAULT nextval('public."SALON_ID_SALON_seq"'::regclass);


--
-- Data for Name: ALUMNO; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."ALUMNO" ("NOMBRE", "EDAD", "ID_ALUMNO", "CORRE0") FROM stdin;
\.


--
-- Data for Name: CURSO; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."CURSO" ("ID_CURSO", "NOMBRE") FROM stdin;
\.


--
-- Data for Name: MALLA_CURRICULAR; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."MALLA_CURRICULAR" ("ID_PROFESOR_CURSO", "ID_PERIODO", "ID_SALON", "ID_MALLA_CURRICULAR") FROM stdin;
\.


--
-- Data for Name: NOTA; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."NOTA" ("ID_MALLA_CURRICULAR", "NOTA", "ID_ALUMNO", "ID_NOTA") FROM stdin;
\.


--
-- Data for Name: PERIODO_ESCOLAR; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."PERIODO_ESCOLAR" ("AÑO", "CICLO", "FECHA_DESDE", "FECHA_HASTA", "ID_PERIODO") FROM stdin;
\.


--
-- Data for Name: PROFESOR; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."PROFESOR" ("ID_PROFESOR", "NOMBRE", "EDAD", "CORREO") FROM stdin;
\.


--
-- Data for Name: PROFESOR_CURSO; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."PROFESOR_CURSO" ("ID_CURSO", "ID_PROFESOR", "ID_PROFESOR_CURSO") FROM stdin;
\.


--
-- Data for Name: SALON; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."SALON" ("ID_SALON", "NOMBRE") FROM stdin;
\.


--
-- Name: ALUMNO_ID_ALUMNO_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."ALUMNO_ID_ALUMNO_seq"', 1, true);


--
-- Name: CURSO_ID_CURSO_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."CURSO_ID_CURSO_seq"', 1, false);


--
-- Name: MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."MALLA_CURRICULAR_ID_MALLA_CURRICULAR_seq"', 1, false);


--
-- Name: NOTA_ID_NOTA_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."NOTA_ID_NOTA_seq"', 1, false);


--
-- Name: PERIODO_ESCOLAR_ID_PERIODO_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."PERIODO_ESCOLAR_ID_PERIODO_seq"', 1, false);


--
-- Name: PROFESOR_CURSO_ID_PROFESOR_CURSO_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."PROFESOR_CURSO_ID_PROFESOR_CURSO_seq"', 1, false);


--
-- Name: PROFESOR_ID_PROFESOR_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."PROFESOR_ID_PROFESOR_seq"', 1, false);


--
-- Name: SALON_ID_SALON_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."SALON_ID_SALON_seq"', 1, false);


--
-- Name: ALUMNO PK_ALUMNO; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ALUMNO"
    ADD CONSTRAINT "PK_ALUMNO" PRIMARY KEY ("ID_ALUMNO");


--
-- Name: CURSO PK_CURSO; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."CURSO"
    ADD CONSTRAINT "PK_CURSO" PRIMARY KEY ("ID_CURSO");


--
-- Name: MALLA_CURRICULAR PK_MALLA_CURRICULAR; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MALLA_CURRICULAR"
    ADD CONSTRAINT "PK_MALLA_CURRICULAR" PRIMARY KEY ("ID_MALLA_CURRICULAR");


--
-- Name: NOTA PK_NOTA; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NOTA"
    ADD CONSTRAINT "PK_NOTA" PRIMARY KEY ("ID_NOTA");


--
-- Name: PERIODO_ESCOLAR PK_PERIODO_ESCOLAR; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PERIODO_ESCOLAR"
    ADD CONSTRAINT "PK_PERIODO_ESCOLAR" PRIMARY KEY ("ID_PERIODO");


--
-- Name: PROFESOR PK_PROFESOR; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PROFESOR"
    ADD CONSTRAINT "PK_PROFESOR" PRIMARY KEY ("ID_PROFESOR");


--
-- Name: PROFESOR_CURSO PK_PROFESOR_CURSO; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PROFESOR_CURSO"
    ADD CONSTRAINT "PK_PROFESOR_CURSO" PRIMARY KEY ("ID_PROFESOR_CURSO");


--
-- Name: SALON PK_SALON; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SALON"
    ADD CONSTRAINT "PK_SALON" PRIMARY KEY ("ID_SALON");


--
-- Name: MALLA_CURRICULAR FK_MALLA_CURRICULAR_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MALLA_CURRICULAR"
    ADD CONSTRAINT "FK_MALLA_CURRICULAR_1" FOREIGN KEY ("ID_PROFESOR_CURSO") REFERENCES public."PROFESOR_CURSO"("ID_PROFESOR_CURSO") NOT VALID;


--
-- Name: MALLA_CURRICULAR FK_MALLA_CURRICULAR_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MALLA_CURRICULAR"
    ADD CONSTRAINT "FK_MALLA_CURRICULAR_2" FOREIGN KEY ("ID_PERIODO") REFERENCES public."PERIODO_ESCOLAR"("ID_PERIODO") NOT VALID;


--
-- Name: MALLA_CURRICULAR FK_MALLA_CURRICULAR_3; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MALLA_CURRICULAR"
    ADD CONSTRAINT "FK_MALLA_CURRICULAR_3" FOREIGN KEY ("ID_SALON") REFERENCES public."SALON"("ID_SALON") NOT VALID;


--
-- Name: NOTA FK_NOTA_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NOTA"
    ADD CONSTRAINT "FK_NOTA_1" FOREIGN KEY ("ID_ALUMNO") REFERENCES public."ALUMNO"("ID_ALUMNO") NOT VALID;


--
-- Name: NOTA FK_NOTA_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NOTA"
    ADD CONSTRAINT "FK_NOTA_2" FOREIGN KEY ("ID_MALLA_CURRICULAR") REFERENCES public."MALLA_CURRICULAR"("ID_MALLA_CURRICULAR") NOT VALID;


--
-- Name: PROFESOR_CURSO FK_PROFESOR_CURSO_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PROFESOR_CURSO"
    ADD CONSTRAINT "FK_PROFESOR_CURSO_1" FOREIGN KEY ("ID_CURSO") REFERENCES public."CURSO"("ID_CURSO") NOT VALID;


--
-- Name: PROFESOR_CURSO FK_PROFESOR_CURSO_2; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PROFESOR_CURSO"
    ADD CONSTRAINT "FK_PROFESOR_CURSO_2" FOREIGN KEY ("ID_PROFESOR") REFERENCES public."PROFESOR"("ID_PROFESOR") NOT VALID;


--
-- PostgreSQL database dump complete
--

