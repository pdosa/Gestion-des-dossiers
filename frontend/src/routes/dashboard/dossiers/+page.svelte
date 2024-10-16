<script lang="ts">
	import InfoDossier, { type Fichier } from '../../../lib/components/InfoDossier.svelte';
	const fichiers: Fichier[] = [
		{ name: 'RVC', status: 'complete' },
		{ name: 'BL', status: 'pending' },
		{ name: 'BESC', status: 'pending' },
		{ name: 'DI', status: 'rejected' }
	];
</script>
<div class="flex flex-wrap justify-evenly">
	<InfoDossier nom="Dossier maritime" {fichiers} transport="maritime" />
	<InfoDossier nom="Dossier aérien" fichiers={fichiers.slice(1)} transport="aérien" />
	<InfoDossier fichiers={[fichiers[0]]} />
</div>
