PGDMP      +            
    {            project    16.0    16.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24589    project    DATABASE     z   CREATE DATABASE project WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
    DROP DATABASE project;
                postgres    false            �            1259    32784    propertydata    TABLE     �  CREATE TABLE public.propertydata (
    owner character varying(40) NOT NULL,
    district character varying(40) NOT NULL,
    taluk character varying(40) NOT NULL,
    type character varying(50) NOT NULL,
    age character varying(40) NOT NULL,
    mobile character varying(40) NOT NULL,
    bedrooms numeric(40,1) NOT NULL,
    sqft double precision NOT NULL,
    description character varying(50) NOT NULL,
    price double precision NOT NULL,
    property_id integer NOT NULL
);
     DROP TABLE public.propertydata;
       public         heap    postgres    false            �            1259    40991    propertydata_property_id_seq    SEQUENCE     �   CREATE SEQUENCE public.propertydata_property_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.propertydata_property_id_seq;
       public          postgres    false    215            �           0    0    propertydata_property_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.propertydata_property_id_seq OWNED BY public.propertydata.property_id;
          public          postgres    false    216            �            1259    40999    querybox    TABLE     �   CREATE TABLE public.querybox (
    query_id integer NOT NULL,
    name character varying(20) NOT NULL,
    mobile_number character varying(20) NOT NULL,
    property_id integer NOT NULL,
    query character varying(50) NOT NULL
);
    DROP TABLE public.querybox;
       public         heap    postgres    false            �            1259    40998    querybox_query_id_seq    SEQUENCE     �   CREATE SEQUENCE public.querybox_query_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.querybox_query_id_seq;
       public          postgres    false    218            �           0    0    querybox_query_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.querybox_query_id_seq OWNED BY public.querybox.query_id;
          public          postgres    false    217            U           2604    40992    propertydata property_id    DEFAULT     �   ALTER TABLE ONLY public.propertydata ALTER COLUMN property_id SET DEFAULT nextval('public.propertydata_property_id_seq'::regclass);
 G   ALTER TABLE public.propertydata ALTER COLUMN property_id DROP DEFAULT;
       public          postgres    false    216    215            V           2604    41002    querybox query_id    DEFAULT     v   ALTER TABLE ONLY public.querybox ALTER COLUMN query_id SET DEFAULT nextval('public.querybox_query_id_seq'::regclass);
 @   ALTER TABLE public.querybox ALTER COLUMN query_id DROP DEFAULT;
       public          postgres    false    217    218    218            �          0    32784    propertydata 
   TABLE DATA           �   COPY public.propertydata (owner, district, taluk, type, age, mobile, bedrooms, sqft, description, price, property_id) FROM stdin;
    public          postgres    false    215   �       �          0    40999    querybox 
   TABLE DATA           U   COPY public.querybox (query_id, name, mobile_number, property_id, query) FROM stdin;
    public          postgres    false    218   $       �           0    0    propertydata_property_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.propertydata_property_id_seq', 992, true);
          public          postgres    false    216            �           0    0    querybox_query_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.querybox_query_id_seq', 8, true);
          public          postgres    false    217            X           2606    40997    propertydata propertydata_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.propertydata
    ADD CONSTRAINT propertydata_pkey PRIMARY KEY (property_id);
 H   ALTER TABLE ONLY public.propertydata DROP CONSTRAINT propertydata_pkey;
       public            postgres    false    215            Z           2606    41004    querybox querybox_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.querybox
    ADD CONSTRAINT querybox_pkey PRIMARY KEY (query_id);
 @   ALTER TABLE ONLY public.querybox DROP CONSTRAINT querybox_pkey;
       public            postgres    false    218            �   
  x�uY�r�H=_Q?0�ڗ#��mI�	w̥,bD� � A��_?/ 	��mYr�r{Krv�y�#{���<�+������������u�x}��2S�,(������K�9�9�����Tf8�*�?u���u6[��*�bv�(��j&D�f^x�W�B4#e��m��6�r�)��-��|�e|���.�[���9��۶͞�oo,dV�`x��,s!۔�����G�\�P�?�x�u]4�Ϫ��i��j۾��񳜅`��Bg�t�x\]���H�����򻲮��]�M�>5����<i��9S��)��j��1B)D��׸YU�2����6�ۮ~"R��Ό�LY˄�<%l�:O�Jz�����,�O�u��}�"��$���3���Dꪞ�*�U��Tm~S�_7�.��s�#�����8�Ǵ���%�֒���V���RqS�ǂ�o���7qY��j�g��A`. ՀޥAAO�RVX]�q>�������4�)�f��P��i�i�,8ˤ��p'R��7�����AC�g�U�[g7-���CC��1�V3)������9s����1,�Ug7�n���}����z�OZ$$�Ҏ)cd��	�<iE��\�eܶ�kl��]\��
˲~��1i*�̡/\�~���5�5�2�h�:�g��k�_��^DZ�!s�9�
��!�U�Q��)+
I����i�[l�}\�w�F��
�^��L:�,�x{d�=5�T	(ut�Г�B�Q�:�|����a$M"��<a�:t�4s)�����j�xiD�o��`n�����6�d� m�a���r�t�D)Z@Κ^���˸Af�U����u�D�c���n�Ƽ�h����'�YgOm�.bU��8�������1!���|
e�xi�t���L1�b������t���5:����S��k�6�1�w@�r�Q�e\�����K�
�ȱ���~!�����{��u�џ�K�}�6q� Z �d(�b���߉܁C�I�k��]�I��dc�y"����0�߫�[�`"����I��`/���ɓ]w����粚��]����A5��I٧9R�<{���w�n⼧�_�����e<歉��f:��? ��mp,.O3��]v�>��fO��5����(Y�Z� q��xу�"�i��0��7-�kM��f^2�H`N{fP=L2v �B 8��gu�w���'b�ﱮ���Ȯ�3�QI��<uk�Q}�eܶ�c��o�<���B˼�C�!��v QJ��ծ��>��T
��L�-�J�ӓ�v�)Q M ��m���]51���e��?E�:AC�zH�v�d��s��*J���r�i#��q^����b��F�}?9��q�%TQaQ<)�K�4�EOn�+��a���命���zF9�Yj4���,���5u�F�o�7��y�f�{�U8O:J`��S=�855�(0jR�e���oH��a�:�"�6��&�="1�5�X��:�K�Y�Ρ��O`�E5_���v����� <;ru�PB���JO�([v:�g�����+�Cz�� &�c��.��X��|ߏ�������PF�ch�x��Q�Д��ִ1C�-޺�f_c����ŝ�x��`~�e',���	� }~Y�e�,^6/�[�<P�e<��i�4c�l�Tf4���;0�rY��r����[�����6E�1�N���:qB�!��
����"�mW�[$M-�� gΣ�Ѓa�8p�E�۟`���hV����X��i�������xF_R�PX�o�s���ˏx4\��$4 ��W'���)��?����6�e�_�.f������vX? ��o0f�`�@i
����������0���W�4н C�MϮj�ͥ����ݪ�3�i�y���-�s����oA���~��3�]�b�0SYTt���E��'q4(A1X-�/�Q�x1� �
h��5ӝ"������n_Bv�$��;P��-G4�'[ѿ�N��v]\9H��$)7�	mG	�a$8%�$��\�������k0�^���x�\�(����/6�5��cP��3V	%F�y� �a#�a���|�����58ԠE�llA�x`lϵ�%�˂���N�d����E��k�N=o��+m��es�6L<���r�2(?u.�.4�Oa�[L��;��<%?V�]@H�qڜ֦	<�
+�u����*�)�!�%�a�dyj3Kc�m�6�ЅM�?ۆ!Y+B������{������fы����!e���N�ԣĚ(z�`DL����%�
���� �`�v�<��+�>&�!b���������_��$ �'���+t�����7�L`���:|�����Q�C���p��S�7�vr�B(f��7u�L��㦷�&�4���"v��P*��1�2�A9�H4kYc ��32���=
x�h�-П�/�o��X/�C��h02�"e�����B��T6Q
e�[Z���`�X�-�k�}�nf���|<$L2"���P�43'n�+(�`t>�n�c$vWvm=Yu�S�Eg*��@���;��������
������9j��9�a!���v�#��~B����MۦX[�@��h��r�L�*`~�^�1�i�-�G(�?/�v��l�/Bē�!=��n} Fu���-`��L
'�G�
�MW+J�s�A�v@m�X�.t=Nh?�)�� �	Ȅ����-���㗫����xZ�J{l�%���[�l���8e!���q״=��� ��QH<¨&J�ĆDW*q��l7$�S��L��b��t�P��Ϝ��O�$�[�W�$��uA��x0��7�?8opF��q�I 	D �M��J8����J\�+��d<�QhO@��CS8���哯�:�^�n�`��U!�ۣH6X=��j����z�-�ܖV�[Tq���n��
������^�$=�!��$�2ӞP<�[n|���X��#���f��o����e�s?T�M����=�04��?�00[�i�������@\�To�o��b},���=�=�� �X�-�vq}Dpv;=X��A4�Z%�m��d���$z��?	���Gl�NANM���@��|�Y�e��@��t��B�Ĳ��V�k,"4>��ӑ���أ���U��r��lK
%m�;���*��5��X �H�:V��kN�t1��B	�8��F7�(2^������������_ᅋ�&�|�nH�Me#*��3�\���|�}�o���*k2�,gMm�;;��ǆ�Ն�3��a��i+��#�$�.ͯ�?��L���$F�ar&�bH�D�΂�1���[x���υ�H����7\S���&a���)__�	џtߛ\h�D�<T�G�ב�w>������+����6k=܋�J�L�0�	���i�`��m�7��O�	�~t�g 9�7({`�)S� �L�s��J��y�c�����g� 2}@�\�@���"��^��>����2��F������/a$/$���R����hM���lBF� r5 ��?�h�������-�"��n^�'�T��H�8�PMs�J5F��3^�#�]]���$Sʲ�vGC�}�K7C;�25���.6���13�솖�����e�t�#�@��֙��>����$*�c>j�:uy��t�� Sm�p��'z̢��L�]��|/;Lv��nn���M�@UxE�D�y�2%8���}��/J��|�6&EZ�8:��~���%]K9�|��V}H��`
�Z�B�����$�ǶRKi}h�������W�4      �   �   x���Aj�0EףS�	BdY��Q��*X"P��I�D��%	�}�h-Yt�g�y��ӑh!E)K^ρ+��t��6^"�c�����zZ[\ٞ�.��S@��ɮ�������g�u�`�:�.���`��Oί�G���JMB.�������0�=��Һ�{��9c�cNC��~I���+�c�bڳ�@�~v��_�63��'>CU:     