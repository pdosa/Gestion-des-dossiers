<script lang="ts">
	import InfoDossier, { type Fichier } from '../../../lib/components/InfoDossier.svelte';
	const fichiers: Fichier[] = [
		{ name: 'RVC', status: 'complete' },
		{ name: 'BL', status: 'pending' },
		{ name: 'BESC', status: 'pending' },
		{ name: 'DI', status: 'rejected' }
	];
</script>

<InfoDossier {fichiers} />
